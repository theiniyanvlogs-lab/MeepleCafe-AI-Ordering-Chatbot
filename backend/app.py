"""
=========================================================
Meeple Cafe AI Ordering Chatbot
FastAPI Application
Version : 1.0
=========================================================
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import chatbot
try:
    # Works when imported as: from backend.app import app
    from backend.chatbot import CafeChatbot
except ImportError:
    # Works when running: python backend/app.py
    from chatbot import CafeChatbot


# ==========================================================
# Create FastAPI App
# ==========================================================

app = FastAPI(
    title="Meeple Cafe AI Ordering Chatbot",
    description="AI Powered Restaurant Ordering Assistant",
    version="1.0"
)

# ==========================================================
# Enable CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# Initialize Chatbot
# ==========================================================

chatbot = CafeChatbot()

# ==========================================================
# Request Model
# ==========================================================

class ChatRequest(BaseModel):
    message: str


# ==========================================================
# Response Model
# ==========================================================

class ChatResponse(BaseModel):
    success: bool
    response: str


# ==========================================================
# Home
# ==========================================================

@app.get("/")
def home():

    return {
        "success": True,
        "application": "Meeple Cafe AI Ordering Chatbot",
        "version": "1.0",
        "status": "Running"
    }


# ==========================================================
# Ping
# ==========================================================

@app.get("/ping")
def ping():

    return {
        "success": True,
        "message": "pong"
    }


# ==========================================================
# Info
# ==========================================================

@app.get("/info")
def info():

    return {

        "Project": "Meeple Cafe AI Ordering Chatbot",

        "Backend": "FastAPI",

        "Vector Database": "FAISS",

        "Embedding Model": "Sentence Transformers",

        "Database": "SQLite"

    }


# ==========================================================
# Chat
# ==========================================================

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        reply = chatbot.chat(request.message)

        return ChatResponse(
            success=True,
            response=reply
        )

    except Exception as e:

        return ChatResponse(
            success=False,
            response=str(e)
        )


# ==========================================================
# Run Server
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
