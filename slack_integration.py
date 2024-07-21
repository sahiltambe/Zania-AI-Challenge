import requests
from config import SLACK_WEBHOOK_URL

# This function sends a message to Slack using a webhook URL
# The message is sent as a JSON payload with the key "text"
# The value of "text" is the message to be sent
# If the request to Slack is successful (status code 200), the function returns without doing anything
# If the request to Slack fails (status code is not 200), the function raises a ValueError with an error message
# The error message includes the status code and the response text from Slack
def post_to_slack(message):
    # Create a dictionary with the key "text" and the value of the message
    payload = {"text": message}
    
    # Send a POST request to the Slack webhook URL with the payload as JSON
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    
    # Check if the response status code is 200 (success)
    if response.status_code != 200:
        # If it's not 200, raise a ValueError with an error message
        # The error message includes the status code and the response text from Slack
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")


# import requests
# import json

# SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'

# def post_to_slack(answers):
#     payload = {
#         "text": json.dumps(answers, indent=4)
#     }
#     requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload))
