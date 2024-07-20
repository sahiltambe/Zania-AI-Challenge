# Zania-AI-Challenge
# PDF Question Answering Agent

This project creates an AI agent that extracts answers from a PDF document based on given questions and posts the results on Slack using OpenAI's GPT-3.5 model.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sahiltambe/Zania-AI-Challenge.git
   cd Zania-AI-Challenge


1. Install the required packages:
   ```bash
   pip install -r requirements.txt



1. Create a .env file and add your OpenAI API key and Slack webhook URL:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   SLACK_WEBHOOK_URL=your_slack_webhook_url



## Usage

To run the program, use the following command:
   ```bash
    python main.py handbook.pdf "What is the name of the company?" "Who is the CEO of the company?"


