import os
import faiss
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceInstructEmbeddings

# Initialize HuggingFaceInstructEmbeddings
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "faiss_index_vector_database"

def store_embeddings(text):
    """
    Store embeddings of chunks of text in a local FAISS vector database.

    Args:
        text (str): The text to store embeddings for.
    """
    # Split text into chunks
    chunks = text.split('. ')

    # Create a list of documents, where each document is a dictionary with 'text' key
    documents = [{"text": chunk} for chunk in chunks]

    # Create a FAISS instance for vector database from documents
    # The vector database will be stored locally in the file specified by vectordb_file_path
    vectordb = FAISS.from_documents(documents=documents, embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)

def query_embeddings(question):
    """
    Query the FAISS vector database for the most relevant documents to a given question.

    Args:
        question (str): The question to query the vector database with.

    Returns:
        list: A list of retrieved documents from the vector database, sorted by relevance.
    """

    # Load the vector database from the local folder
    # The vector database is a FAISS instance that contains embeddings of text chunks
    # The vector database is loaded using the file path specified by vectordb_file_path
    # The vector database uses the HuggingFaceInstructEmbeddings model for embedding text chunks
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings)

    # Create a retriever for querying the vector database
    # The retriever is configured to return results with a score above a threshold of 0.2
    # The retriever uses the FAISS vector database for querying
    retriever = vectordb.as_retriever(score_threshold=0.2)

    # Query the vector database for answers
    # The retriever.retrieve method takes a question as input and returns a list of retrieved documents
    # The retrieved documents are sorted by relevance to the question
    results = retriever.retrieve(question)

    # Return the list of retrieved documents
    return results
