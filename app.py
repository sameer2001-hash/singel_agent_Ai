from fastapi import FastAPI
from chatbot import get_chat_response
from schema import ChatRequest, ChatResponse

app = FastAPI(
    title="Single Agent Chatbot",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "Single Agent Chatbot is Running"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    reply = get_chat_response(request.message)

    return ChatResponse(reply=reply)