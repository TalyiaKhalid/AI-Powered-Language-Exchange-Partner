from ollama import chat
from ollama import ChatResponse
from groq import Groq
import os
import re
from dotenv import load_dotenv


# Load the .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("GROQ_API_KEY")

user_input = input("\n: ")

# with punctuations

# prompt = f"""
# You are an expert in English grammar. You are given a learner’s input.
# Your task is to provide the corrected version of the input. 
# Do not give any feedback or suggestions, just return the corrected version.

# Input: {user_input}
# Response:
# """

# without punctuations

prompt = f"""
You are an expert in English grammar. You are given a learner’s input.
Your task is to provide the corrected version of the input, ignoring any punctuation.
Do not give any feedback or suggestions, just return the corrected version without punctuation affecting the correction.

Input: {user_input}
Response:
"""


messages = [
  {
    'role': 'user',
    'content': prompt,
  }
]

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

chat_completion = client.chat.completions.create(
    messages=messages,
    model="llama-3.3-70b-versatile" # "llama-3.3-70b-versatile or deepseek-r1-distill-llama-70b"
)

response = chat_completion.choices[0].message.content


print(response)