"""
=========================================================
Meeple Cafe AI Ordering Chatbot
FastAPI Application
Version: 1.0
=========================================================
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# chatbot controller
from chatbot import RestaurantChatbot


# --------------------------------------------------------
# Initialize FastAPI
# --------------------------------------------------------

app = FastAPI(
    title="Meeple Cafe AI Ordering Chatbot",
    description="AI Powered Restaurant Ordering Assistant",
    version="1.0.0"
)

# --------------------------------------------------------
# Enable CORS
# --------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------------
# Initialize Chatbot
# --------------------------------------------------------

chatbot = RestaurantChatbot()

# --------------------------------------------------------
# Request Model
# --------------------------------------------------------

class ChatRequest(BaseModel):
    message: str
    session_id: str = "guest"


# --------------------------------------------------------
# Root Endpoint
# --------------------------------------------------------

@app.get("/")
def home():
    return {
        "application": "Meeple Cafe AI Ordering Chatbot",
        "version": "1.0",
        "status": "Running"
    }


# --------------------------------------------------------
# Health Check
# --------------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


# --------------------------------------------------------
# Chat Endpoint
# --------------------------------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    reply = chatbot.get_response(
        request.message,
        request.session_id
    )

    return {
        "reply": reply
    }


# --------------------------------------------------------
# Future APIs
# --------------------------------------------------------

@app.get("/menu")
def menu():
    """
    Return complete menu.
    """
    return {
        "message": "Coming Soon"
    }


@app.get("/cart")
def cart():
    """
    Return customer cart.
    """
    return {
        "message": "Coming Soon"
    }


@app.post("/checkout")
def checkout():
    """
    Place order.
    """
    return {
        "message": "Coming Soon"
    }


# --------------------------------------------------------
# Run Server
# --------------------------------------------------------

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
