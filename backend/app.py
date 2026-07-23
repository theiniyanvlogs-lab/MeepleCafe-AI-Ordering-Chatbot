"""
=========================================================
Meeple Cafe AI Ordering Chatbot
FastAPI Backend
Version : 3.0.0
Author  : Sugumar R
=========================================================
"""

from contextlib import asynccontextmanager
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ==========================================================
# Backend Imports
# ==========================================================

from backend.config import (
    API_TITLE,
    API_VERSION,
    API_DESCRIPTION,
    ALLOWED_ORIGINS,
    RESTAURANT_NAME,
    RESTAURANT_PHONE,
    RESTAURANT_EMAIL,
    OPENING_HOURS,
)

from backend.chatbot import CafeChatbot
from backend.search_engine import SearchEngine
from backend.ordering import OrderManager
from backend.rag import rag_engine
from backend.memory import memory
from backend.utils import (
    current_datetime,
    health_status,
    success_response,
)

# ==========================================================
# Initialize Services
# ==========================================================

chatbot = CafeChatbot()
search_engine = SearchEngine()
order_manager = OrderManager()

# ==========================================================
# Application Lifespan
# ==========================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("=" * 60)
    print("🚀 Starting Meeple Cafe AI Ordering Chatbot")
    print("=" * 60)

    try:
        print("✅ Chatbot Loaded")
        print("✅ Search Engine Loaded")
        print("✅ Order Manager Loaded")
        print("✅ RAG Engine Loaded")
        print("✅ Conversation Memory Loaded")

    except Exception as e:
        print(f"❌ Startup Error: {e}")

    yield

    print("=" * 60)
    print("🛑 Application Shutdown")
    print("=" * 60)

# ==========================================================
# FastAPI
# ==========================================================

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description=API_DESCRIPTION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# ==========================================================
# CORS
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================================
# Request Models
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
# Response Models
# ==========================================================

class HealthResponse(BaseModel):
    status: str
    version: str
    server_time: str


class InfoResponse(BaseModel):
    application: str
    version: str
    restaurant: str
    status: str

# ==========================================================
# Root
# ==========================================================

@app.get("/")
def home():

    return {
        "application": API_TITLE,
        "version": API_VERSION,
        "status": "Running",
        "restaurant": RESTAURANT_NAME,
        "documentation": "/docs",
        "health": "/health",
    }


# ==========================================================
# Health Check
# ==========================================================

@app.get(
    "/health",
    response_model=HealthResponse,
)
def health():

    return HealthResponse(
        status="Healthy",
        version=API_VERSION,
        server_time=current_datetime(),
    )


# ==========================================================
# API Information
# ==========================================================

@app.get(
    "/info",
    response_model=InfoResponse,
)
def info():

    return InfoResponse(
        application=API_TITLE,
        version=API_VERSION,
        restaurant=RESTAURANT_NAME,
        status="Running",
    )


# ==========================================================
# Restaurant Information
# ==========================================================

@app.get("/restaurant")
def restaurant():

    return success_response(
        {
            "name": RESTAURANT_NAME,
            "phone": RESTAURANT_PHONE,
            "email": RESTAURANT_EMAIL,
            "opening_hours": OPENING_HOURS,
            "generated_at": current_datetime(),
        }
    )


# ==========================================================
# Complete Menu
# ==========================================================

@app.get("/menu")
def get_menu():

    try:

        menu = search_engine.get_all_menu()

        return success_response(
            {
                "total_items": len(menu),
                "menu": menu,
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to load menu: {e}",
        )


# ==========================================================
# Search Menu
# ==========================================================

@app.get("/menu/search")
def search_menu(q: str):

    try:

        results = search_engine.search(q)

        return success_response(
            {
                "query": q,
                "count": len(results),
                "results": results,
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Search failed: {e}",
        )

# ==========================================================
# AI Chat
# ==========================================================

@app.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    try:

        answer = chatbot.chat(request.message)

        return ChatResponse(
            answer=answer
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Chatbot Error: {e}",
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

        return success_response(
            {
                "order_id": order_id,
                "status": "Preparing",
                "message": "Your order has been placed successfully.",
                "created_at": current_datetime(),
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Order Error: {e}",
        )


# ==========================================================
# Order History
# ==========================================================

@app.get("/orders")
def get_orders():

    try:

        orders = order_manager.get_orders()

        return success_response(
            {
                "total_orders": len(orders),
                "orders": orders,
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Unable to retrieve orders: {e}",
        )


# ==========================================================
# Statistics
# ==========================================================

@app.get("/stats")
def statistics():

    try:

        return success_response(
            {
                "chat_sessions": memory.total_sessions(),
                "messages": memory.total_messages(),
                "vector_documents": rag_engine.vector_store.size(),
                "orders": len(order_manager.get_orders()),
                "server_time": current_datetime(),
            }
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Statistics Error: {e}",
        )


# ==========================================================
# Ping
# ==========================================================

@app.get("/ping")
def ping():

    return {
        "message": "pong",
        "time": current_datetime(),
    }


# ==========================================================
# Run Application
# ==========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "backend.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )

