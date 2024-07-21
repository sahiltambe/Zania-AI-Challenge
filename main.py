import sys
from pdf_reader import extract_text_from_pdf
from question_answering import get_answers_from_text
from slack_integration import post_to_slack
from utils import format_answers_as_json

def main(pdf_file, questions):
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(pdf_file)

    # text = """
    #         Welcome! You have just joined a dedicated organization. We hope that your employment with Zania, Inc. will be rewarding and challenging. We take pride in our employees as well as in the products and services we provide. The Company complies with all federal and state employment laws, and this handbook generally reflects those laws. The Company also complies with any applicable local laws, although there may not be an express written policy regarding those laws contained in the handbook. 
    #         The employment policies and/or benefits summaries in this handbook are written for all employees. When questions arise concerning the interpretation of these policies as they relate to employees who are covered by a collective-bargaining agreement, the answers will be determined by reference to the actual union contract, rather than the summaries contained in this handbook. Please take the time now to read this handbook carefully. Sign the acknowledgment at the end to show that you have read,
    #         understood, and agree to the contents of this handbook, which sets out the basic rules and guidelines concerning your employment. This handbook supersedes any previously issued handbooks or policy statements dealing with the subjects discussed herein. The Company reserves the right to interpret, modify, or supplement the provisions of this handbook at any time. Neither this handbook nor any other communication by a management representative or other, whether oral or written, is intended in any way to create a contract of employment. Please understand that no employee handbook can address
    #         every situation in the work place. If you have questions about your employment or any provisions in this handbook, contact People Operations.We wish you success in your employment here at Zania, Inc.!
    #         All the best,
    #         Shruti Gupta, CEO
    #         Zania, Inc.
    # """

    # Step 2: Get answers from text using OpenAI
    answers = get_answers_from_text(text, questions)

    # Step 3: Format answers as JSON
    answers_json = format_answers_as_json(answers)

    # Step 4: Post to Slack
    post_to_slack(answers_json)

    print("Answers posted to Slack successfully!")

if __name__ == "__main__":
    pdf_file = sys.argv[1]
    questions = sys.argv[2:]
    main(pdf_file, questions)


# from question_answering import get_answers_from_text, get_answers_from_embeddings
# from slack_integration import post_to_slack
# from utils import format_answers_as_json
# import sys
# from pdf_reader import extract_text_from_pdf
# from embedder import store_embeddings

# def extract_text(pdf_file):
#     """
#     Extract text from a PDF file.

#     Args:
#         pdf_file (str): Path to the PDF file.

#     Returns:
#         str: Text extracted from the PDF.
#     """
#     # Use the pdf_reader module to extract text from the PDF file
#     return extract_text_from_pdf(pdf_file)

# def get_answers(text, questions):
#     """
#     Get answers from the given text using OpenAI.

#     This function takes in the text and questions as input and returns
#     the answers to the questions. It first stores the embeddings of the
#     text using the `store_embeddings` function from the `embedder` module.
#     Then, it calls the `get_answers_from_embeddings` function from the
#     `question_answering` module to query the vector database for answers.

#     Args:
#         text (str): The text from which answers are to be extracted.
#         questions (list): List of questions for which answers are needed.

#     Returns:
#         dict: A dictionary mapping each question to its corresponding answer.
#     """
#     # Store the embeddings of the text using the OpenAI embedder
#     store_embeddings(text)
    
#     # Query the vector database for answers to the given questions
#     # using the OpenAI model
#     return get_answers_from_embeddings(text, questions)

# def post_answers_to_slack(answers):
#     """
#     Posts the answers to Slack.

#     Args:
#         answers (dict): A dictionary mapping questions to answers.

#     Returns:
#         None
#     """
#     # Post the answers to Slack using the post_to_slack function
#     # from the slack_integration module
#     post_to_slack(answers)

# def main(pdf_file, questions):
#     """
#     Main function that extracts text from a PDF file, gets answers from the text,
#     and posts the answers to Slack.

#     Args:
#         pdf_file (str): Path to the PDF file.
#         questions (list): List of questions for which answers are needed.

#     Returns:
#         None
#     """
#     # Extract text from the PDF file
#     text = extract_text(pdf_file)

#     # Get answers from the text using OpenAI
#     answers = get_answers(text, questions)

#     # Post the answers to Slack
#     post_answers_to_slack(answers)

#     # Print success message
#     print("Answers posted to Slack successfully!")

# if __name__ == "__main__":
#     pdf_file = sys.argv[1]
#     questions = sys.argv[2:]
#     main(pdf_file, questions)
