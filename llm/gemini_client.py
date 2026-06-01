import google.generativeai as genai
from config.settings import GEMINI_API_KEY, MODEL_NAME
from utils.logger import logger
from utils.exceptions import GeminiAPIError


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(MODEL_NAME)


def generate_response(prompt: str):

    try:

        logger.info("Sending request to Gemini")

        response = model.generate_content(prompt)

        logger.info("Gemini response received")

        return response.text

    except Exception as e:

        logger.error(str(e))

        raise GeminiAPIError(
            f"Gemini request failed: {str(e)}"
        )

print("API KEY:", GEMINI_API_KEY)
print("MODEL:", MODEL_NAME)