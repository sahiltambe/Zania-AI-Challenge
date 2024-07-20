# from pdf_reader.py import extract_text_from_pdf
import sys
from pdf_reader import extract_text_from_pdf
from question_answering import get_answers_from_text
from slack_integration import post_to_slack
from utils import format_answers_as_json

def main(pdf_file, questions):
    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(pdf_file)
    
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
