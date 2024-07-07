import google.generativeai as genai
genai.configure(api_key='AIzaSyCqfFtifTqd-L3t9lSGMVY6GT46fSfiVZo')


def decode(ciphertext) -> str:
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

    response = chat_session.send_message(f"You are a Pig Latin translator. You have been tasked with translating this piece of text '{ciphertext}' into readable English.")

    return response.text