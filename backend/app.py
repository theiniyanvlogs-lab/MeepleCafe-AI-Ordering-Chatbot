"""
=========================================================
Meeple Cafe AI Ordering Chatbot
FastAPI Backend
Version : 2.0
=========================================================
"""

from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ==========================================================
# Import Backend Modules
# ==========================================================

try:
    from backend.chatbot import CafeChatbot
    from backend.search_engine import SearchEngine
    from backend.ordering import OrderManager
except ImportError:
    from chatbot import CafeChatbot
    from search_engine import SearchEngine
    from ordering import OrderManager

# ==========================================================
# FastAPI
# ==========================================================

app = FastAPI(
    title="Meeple Cafe AI Ordering Chatbot",
    description="AI Powered Restaurant Ordering Assistant",
    version="2.0.0",
)

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# Initialize Services
# ==========================================================

chatbot = CafeChatbot()
search_engine = SearchEngine()
order_manager = OrderManager()

# ==========================================================
# Models
# ==========================================================

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


class OrderItem(BaseModel):
    id: int
    quantity: int


class OrderRequest(BaseModel):
    customer_name: str
    phone: str
    email: Optional[str] = None
    address: str
    payment_method: str
    items: List[OrderItem]


# ==========================================================
# Root
# ==========================================================

@app.get("/")
def home():
    return {
        "application": "Meeple Cafe AI Ordering Chatbot",
        "version": "2.0.0",
        "status": "Running",
    }


# ==========================================================
# Health
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": "2.0.0",
    }


# ==========================================================
# Restaurant Information
# ==========================================================

@app.get("/restaurant")
def restaurant():

    return {
        "name": "Meeple Cafe",
        "address": "Chennai, Tamil Nadu",
        "phone": "+91 9876543210",
        "email": "support@meeplecafe.com",
        "opening_hours": "9:00 AM - 10:00 PM",
    }


# ==========================================================
# Menu
# ==========================================================

@app.get("/menu")
def get_menu():

    try:
        return search_engine.get_all_menu()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ==========================================================
# Search Menu
# ==========================================================

@app.get("/menu/search")
def search_menu(q: str):

    try:
        return search_engine.search(q)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ==========================================================
# AI Chat
# ==========================================================

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        answer = chatbot.chat(request.message)

        return ChatResponse(answer=answer)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================================================
# Place Order
# ==========================================================

@app.post("/order")
def place_order(order: OrderRequest):

    try:

        order_id = order_manager.place_order(
            customer_name=order.customer_name,
            phone=order.phone,
            email=order.email,
            address=order.address,
            payment_method=order.payment_method,
            items=[item.model_dump() for item in order.items],
        )

        return {
            "order_id": order_id,
            "status": "Preparing",
            "message": "Order placed successfully",
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================================================
# Orders
# ==========================================================

@app.get("/orders")
def get_orders():

    try:

        return order_manager.get_orders()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# ==========================================================
# Ping
# ==========================================================

@app.get("/ping")
def ping():

    return {
        "message": "pong"
    }


# ==========================================================
# Run
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
