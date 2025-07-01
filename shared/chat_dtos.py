from pydantic import BaseModel


class ChatRequest(BaseModel):
    content: list[str]
    api_key: str = None  # Accept API key from frontend


class ChatResponse(BaseModel):
    response: str
