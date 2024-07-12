"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python

Get your Google AI API key here:
https://aistudio.google.com/app/apikey
Use your Google account to sign in for the key. (It's free ;) )
"""

import os

import google.generativeai as genai

os.environ["API_KEY"] = ""

genai.configure(api_key=os.environ["API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)
def decode(ciphertext):
    response = chat_session.send_message(f"You are a Pig Latin translator. You have been tasked with translating this piece of text: '{ciphertext}' into readable English.")
    return response.text