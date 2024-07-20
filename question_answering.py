import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_answers_from_text(text, questions):
    answers = {}
    for question in questions:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-0125",
            prompt=f"Based on the following document text:\n{text}\n\nAnswer the question: {question}",
            max_tokens=100,
            temperature=0
        )
        answer = response.choices[0].text.strip()
        if answer.lower() == "data not available" or "i'm sorry" in answer.lower():
            answers[question] = "Data Not Available"
        else:
            answers[question] = answer
    return answers
