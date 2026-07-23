# 🍽️ Meeple Cafe AI Ordering Chatbot

An AI-powered restaurant ordering chatbot built using **FastAPI**, **FAISS**, **Sentence Transformers**, and **Next.js**. The chatbot allows customers to search the menu using natural language, place orders, manage their cart, and interact with an AI-powered restaurant assistant.

---

## 🚀 Features

- 🤖 AI-powered restaurant chatbot
- 🔍 Semantic menu search using FAISS
- 🧠 Retrieval-Augmented Generation (RAG)
- 🍕 Natural language menu search
- 🛒 Shopping cart management
- 📦 Order placement
- 📋 Order history
- 💬 Conversation memory
- ⚡ FastAPI REST API
- 🎨 Modern Next.js frontend
- 📱 Responsive design
- 🔄 Real-time API communication

---

# 🏗️ Project Architecture

```text
                 User
                   │
                   ▼
         Next.js Frontend (React)
                   │
          REST API (FastAPI)
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
  Chatbot      Search Engine   Ordering
      │            │            │
      └───────┬────┴────────────┘
              ▼
          RAG Engine
              │
      ┌───────┴────────┐
      ▼                ▼
  FAISS Index      CSV Dataset
              │
              ▼
         Sentence Transformer
```

---

# 📂 Project Structure

```text
MeepleCafe-AI-Ordering-Chatbot/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── config.py
│   ├── database.py
│   ├── memory.py
│   ├── ordering.py
│   ├── rag.py
│   ├── search_engine.py
│   ├── utils.py
│   └── vector_store.py
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── context/
│   ├── services/
│   └── types/
│
├── data/
│   ├── menu.csv
│   ├── faq.csv
│   ├── restaurant.csv
│   └── orders.db
│
├── vector_db/
│   ├── menu.index
│   └── metadata.pkl
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── .env.example
```

---

# 🛠️ Technology Stack

## Backend

- Python
- FastAPI
- Pydantic
- SQLite
- FAISS
- Sentence Transformers
- Uvicorn

## Frontend

- Next.js 15
- React 19
- TypeScript
- Tailwind CSS
- Context API

## AI / Machine Learning

- RAG (Retrieval-Augmented Generation)
- all-MiniLM-L6-v2
- Semantic Search
- Vector Embeddings

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/MeepleCafe-AI-Ordering-Chatbot.git
cd MeepleCafe-AI-Ordering-Chatbot
```

---

## Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn backend.app:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL

```
http://localhost:3000
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Information |
| GET | `/health` | Health Check |
| GET | `/restaurant` | Restaurant Information |
| GET | `/menu` | Get Complete Menu |
| GET | `/menu/search?q=` | Search Menu |
| POST | `/chat` | AI Chat |
| POST | `/order` | Place Order |
| GET | `/orders` | Order History |
| GET | `/ping` | Ping API |

---

# 💬 Example Queries

```text
Hi

Show burgers

Pizza under ₹300

Veg dishes

Cold coffee

Desserts

Add Veg Burger

View cart

Checkout
```

---

# 📸 Screenshots

Add screenshots after deployment.

```
screenshots/

home.png

chat.png

menu.png

cart.png

checkout.png

orders.png
```

---

# 🚀 Deployment

## Backend

Render

## Frontend

Vercel

---

# 🔮 Future Enhancements

- Voice Ordering
- Online Payments
- User Authentication
- Admin Dashboard
- Table Reservation
- Multi-language Support
- Recommendation Engine
- Order Tracking
- AI Menu Recommendations

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Sugumar R**

MBA | AI Developer | Business Analyst

GitHub:
https://github.com/YOUR_USERNAME

LinkedIn:
https://linkedin.com/in/YOUR_LINKEDIN

Email:

```
contact.sugumarai@gmail.com
```

---

# ⭐ Support

If you like this project, please give it a ⭐ on GitHub.
