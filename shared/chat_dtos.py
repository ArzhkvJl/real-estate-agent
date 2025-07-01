from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from backend.infrastructure.gemini_communication.configuration import GenerationConfig


class MessageCreate(BaseModel):
    content: str = Field(..., description="Content of the message")
    config: Optional[GenerationConfig] = Field(default=None, description="Optional generation configuration")
    api_key: str = Field(..., description="Gemini API key")


class MessageResponse(BaseModel):
    content: str
    role: str


class ChatResponse(BaseModel):
    id: int
    assistant_id: int
    messages: List[MessageResponse]
    
    model_config = ConfigDict(from_attributes=True)


