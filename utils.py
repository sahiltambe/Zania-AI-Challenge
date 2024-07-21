import json

def format_answers_as_json(answers):
    """
    Format answers as JSON string with an indentation of 2 spaces.

    Args:
        answers (dict): A dictionary containing the answers.

    Returns:
        str: A JSON-formatted string representing the answers.
    """
    return json.dumps(answers, indent=2)
