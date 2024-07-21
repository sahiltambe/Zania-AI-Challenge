import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def chunk_text(text, max_tokens=1500):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) > max_tokens:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def get_answers_from_text(text, questions):
    text_chunks = chunk_text(text)
    answers = {}

    for question in questions:
        combined_answer = ""
        for chunk in text_chunks:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0125",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Based on the following document text:\n{chunk}\n\nAnswer the question: {question}"}
                ],
                max_tokens=100,
                temperature=0
            )
            answer = response.choices[0].message['content'].strip()
            if answer.lower() == "data not available" or "i'm sorry" in answer.lower():
                combined_answer = "Data Not Available"
                break
            combined_answer += " " + answer
        answers[question] = combined_answer.strip()
    return answers



# import openai
# from config import OPENAI_API_KEY

# openai.api_key = OPENAI_API_KEY

# def chunk_text(text, max_tokens=1500):
#     """
#     This function takes in a block of text and splits it into chunks of words 
#     that are less than or equal to the specified maximum number of tokens.

#     Args:
#         text (str): The block of text to be chunked.
#         max_tokens (int): The maximum number of tokens (words) per chunk.

#     Returns:
#         list: A list of strings, where each string is a chunk of words.
#     """

#     # Split the text into a list of words
#     words = text.split()

#     # Initialize an empty list to store the chunks of words
#     chunks = []

#     # Initialize an empty list to store the current chunk of words
#     current_chunk = []

#     # Iterate over each word in the list of words
#     for word in words:

#         # Add the word to the current chunk of words
#         current_chunk.append(word)

#         # Check if the length of the current chunk of words is greater than the maximum number of tokens
#         if len(' '.join(current_chunk)) > max_tokens:

#             # If it is, add the current chunk of words to the list of chunks
#             chunks.append(' '.join(current_chunk))

#             # Reset the current chunk of words to an empty list
#             current_chunk = []

#     # Check if there are any remaining words in the current chunk of words
#     if current_chunk:

#         # If there are, add the current chunk of words to the list of chunks
#         chunks.append(' '.join(current_chunk))

#     # Return the list of chunks of words
#     return chunks

# def get_answers_from_text(text, questions):
#     """
#     Get answers to a list of questions based on a block of text.

#     Args:
#         text (str): The block of text to answer the questions with.
#         questions (list): A list of questions to be answered.

#     Returns:
#         dict: A dictionary where the keys are the questions and the values are the answers.
#     """

#     # Split the text into chunks based on the maximum number of tokens per chunk
#     text_chunks = chunk_text(text)

#     # Initialize an empty dictionary to store the answers
#     answers = {}

#     # Iterate over each question
#     for question in questions:

#         # Initialize an empty string to store the combined answer for the current question
#         combined_answer = ""

#         # Iterate over each chunk of text
#         for chunk in text_chunks:

#             # Use OpenAI's GPT-3.5-turbo-0125 model to generate an answer to the question based on the current chunk of text
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo-0125",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": f"Based on the following document text:\n{chunk}\n\nAnswer the question: {question}"}
#                 ],
#                 max_tokens=100,
#                 temperature=0
#             )

#             # Get the answer from the response
#             answer = response.choices[0].message['content'].strip()

#             # Check if the answer is "Data Not Available" or if it contains the phrase "i'm sorry"
#             if answer.lower() == "data not available" or "i'm sorry" in answer.lower():

#                 # If it is, set the combined answer for the current question to "Data Not Available" and break out of the loop
#                 combined_answer = "Data Not Available"
#                 break

#             # Otherwise, add the answer to the combined answer for the current question
#             combined_answer += " " + answer

#         # Remove any leading or trailing whitespace from the combined answer for the current question
#         answers[question] = combined_answer.strip()

#     # Return the dictionary of answers
#     return answers


# import os
# from langchain_community.llms import GooglePalm
# from langchain.prompts import PromptTemplate
# from langchain.chains import RetrievalQA
# from embedder import query_embeddings

# # Set GooglePalm API key from environment variable
# os.environ['GOOGLE_API_KEY'] = "GOOGLE_API_KEY" # Replace with your actual API key

# # Create Google Palm LLM model
# llm = GooglePalm(temperature=0.5)

# def get_answers_from_embeddings(questions):
#     answers = {}
#     for question in questions:
#         results = query_embeddings(question)
#         if not results:
#             answers[question] = "Data Not Available"
#         else:
#             # Assuming results contain the most relevant text chunks
#             relevant_text = results[0].text
#             answers[question] = relevant_text
#     return answers
