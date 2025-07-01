from langchain_google_genai import ChatGoogleGenerativeAI
from shared import constants


def get_llm(api_key: str) -> ChatGoogleGenerativeAI:
    """Integrate the Google AI chat model with the provided API key and default parameters"""
    return ChatGoogleGenerativeAI(
        model=constants.MODEL, 
        temperature=constants.DEFAULT_TEMPERATURE,
        max_tokens=constants.MAX_TOKENS,
        google_api_key=api_key
    )
