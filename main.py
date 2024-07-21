from question_answering import get_answers_from_text, get_answers_from_embeddings
from slack_integration import post_to_slack
from utils import format_answers_as_json
import sys
from pdf_reader import extract_text_from_pdf
from embedder import store_embeddings

def extract_text(pdf_file):
    """
    Extract text from a PDF file.

    Args:
        pdf_file (str): Path to the PDF file.

    Returns:
        str: Text extracted from the PDF.
    """
    # Use the pdf_reader module to extract text from the PDF file
    return extract_text_from_pdf(pdf_file)

def get_answers(text, questions):
    """
    Get answers from the given text using OpenAI.

    This function takes in the text and questions as input and returns
    the answers to the questions. It first stores the embeddings of the
    text using the `store_embeddings` function from the `embedder` module.
    Then, it calls the `get_answers_from_embeddings` function from the
    `question_answering` module to query the vector database for answers.

    Args:
        text (str): The text from which answers are to be extracted.
        questions (list): List of questions for which answers are needed.

    Returns:
        dict: A dictionary mapping each question to its corresponding answer.
    """
    # Store the embeddings of the text using the OpenAI embedder
    store_embeddings(text)
    
    # Query the vector database for answers to the given questions
    # using the OpenAI model
    return get_answers_from_embeddings(text, questions)

def post_answers_to_slack(answers):
    """
    Posts the answers to Slack.

    Args:
        answers (dict): A dictionary mapping questions to answers.

    Returns:
        None
    """
    # Post the answers to Slack using the post_to_slack function
    # from the slack_integration module
    post_to_slack(answers)

def main(pdf_file, questions):
    """
    Main function that extracts text from a PDF file, gets answers from the text,
    and posts the answers to Slack.

    Args:
        pdf_file (str): Path to the PDF file.
        questions (list): List of questions for which answers are needed.

    Returns:
        None
    """
    # Extract text from the PDF file
    text = extract_text(pdf_file)

    # Get answers from the text using OpenAI
    answers = get_answers(text, questions)

    # Post the answers to Slack
    post_answers_to_slack(answers)

    # Print success message
    print("Answers posted to Slack successfully!")

if __name__ == "__main__":
    pdf_file = sys.argv[1]
    questions = sys.argv[2:]
    main(pdf_file, questions)


# import sys
# from pdf_reader import extract_text_from_pdf
# from embedder import store_embeddings, query_embeddings
# from question_answering import get_answers_from_embeddings
# from slack_integration import post_to_slack

# def main(pdf_file, questions):
#     # Step 1: Extract text from PDF
#     text = extract_text_from_pdf(pdf_file)
    
#     # Step 2: Store embeddings in FAISS
#     store_embeddings(text)
    
#     # Step 3: Query the vector database for answers
#     answers = get_answers_from_embeddings(questions)
    
#     # Step 4: Post the results to Slack
#     post_to_slack(answers)

# if __name__ == "__main__":
#     if len(sys.argv) < 3:
#         print("Usage: python main.py <pdf_file> <questions>")
#         sys.exit(1)
    
#     pdf_file = sys.argv[1]
#     questions = sys.argv[2:]
#     main(pdf_file, questions)
