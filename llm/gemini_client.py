import google.generativeai as genai
from config.settings import GEMINI_API_KEY, MODEL_NAME


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

def generate_response(prompt: str):

    response = model.generate_content(prompt)
    return response.text

print("API KEY:", GEMINI_API_KEY)
print("MODEL:", MODEL_NAME)