from pydantic import BaseModel

# Data Transfer Object for chat requests from the frontend to the backend
class ChatRequest(BaseModel):
    content: list[str]  # List of message strings representing the chat history
    api_key: str = None  # Accept API key from frontend

# Data Transfer Object for chat responses from the backend to the frontend
class ChatResponse(BaseModel):
    response: str  # The assistant's response to be displayed in the chat UI
