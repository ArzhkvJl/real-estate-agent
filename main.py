from fastapi import FastAPI
from shared.chat_dtos import ChatRequest, ChatResponse
from app.agent.agent import create_agent

app = FastAPI(
    title="AI Assistant & Real Estate Asset Management API",
    description="""
    This Application provides intelligent assistants for:
    - Real estate asset management via natural language instructions (compare properties, calculate profit & loss, retrieve asset details, and more)
    - Conversational AI assistants based on Google's Gemini models

    Features:
    - Analyze and manage real estate assets using natural language
    - Compare property performance, calculate P&L, and access asset details
    """,
    version="1.0.0")


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    # Create a new LLM instance with the provided API key for each request
    agent = create_agent(req.api_key)
    response = agent.invoke({"messages":  req.content})
    for_analysis = ''
    for message in response['messages']:
        for_analysis = message.content
    return ChatResponse(response=for_analysis)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000, host="127.0.0.1")
    