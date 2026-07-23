# 🍽️ Meeple Cafe AI Ordering Chatbot

An AI-powered restaurant ordering chatbot built with **FastAPI**, **FAISS**, **Sentence Transformers**, and **SQLite**. The chatbot provides intelligent menu search, FAQ assistance, restaurant information, shopping cart management, and order placement using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

### 🤖 AI Restaurant Assistant

- Semantic menu search using FAISS
- Natural language understanding
- Restaurant FAQ assistant
- Restaurant information assistant
- Context-aware conversations

### 🍕 Menu Features

- Browse menu
- Search menu items
- Category-wise search
- Price-based search
- Veg / Non-Veg search
- Food recommendations

### 🛒 Ordering System

- Add items to cart
- Remove items
- View cart
- Calculate GST
- Checkout
- Save orders to SQLite

### 🧠 AI Knowledge Base

- Menu knowledge
- FAQ knowledge
- Restaurant information
- Vector search using embeddings

---

# 🏗️ Project Architecture

```
                 User
                   │
                   ▼
            FastAPI Backend
                   │
         ┌─────────┴─────────┐
         │                   │
         ▼                   ▼
 Conversation Memory      Order Manager
         │                   │
         └─────────┬─────────┘
                   │
                   ▼
               RAG Engine
                   │
                   ▼
             Vector Store
                   │
                   ▼
              FAISS Search
                   │
                   ▼
          menu.index + metadata.pkl
                   │
                   ▼
         Menu + FAQ + Restaurant Data
```

---

# 📂 Project Structure

```
MeepleCafe-AI-Ordering-Chatbot/

backend/
│
├── app.py
├── chatbot.py
├── search_engine.py
├── database.py
├── memory.py
├── ordering.py
├── utils.py
├── config.py
├── build_vector_db.py
├── vector_store.py
└── rag.py

data/
│
├── menu.csv
├── faq.csv
└── restaurant.csv

vector_db/
│
├── menu.index
└── metadata.pkl

requirements.txt
README.md
LICENSE
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| FastAPI | REST API |
| FAISS | Vector Database |
| Sentence Transformers | Embeddings |
| SQLite | Order Database |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Scikit-learn | Utilities |
| Uvicorn | FastAPI Server |

---

# 📊 AI Workflow

```
CSV Files

menu.csv
faq.csv
restaurant.csv

        │

        ▼

build_vector_db.py

        │

Sentence Transformer

        │

Embeddings

        │

FAISS Index

        │

menu.index
metadata.pkl

        │

vector_store.py

        │

RAG Search

        │

Restaurant Chatbot

        │

User Response
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/theiniyanvlogs-lab/MeepleCafe-AI-Ordering-Chatbot.git

cd MeepleCafe-AI-Ordering-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Build Vector Database

Run once whenever the CSV files are updated.

```bash
python backend/build_vector_db.py
```

Generated files

```
vector_db/

menu.index

metadata.pkl
```

---

# ▶️ Run FastAPI

```bash
uvicorn backend.app:app --reload
```

or

```bash
python backend/app.py
```

---

# 💬 Example Questions

```
Show me burgers

Pizza under ₹300

Best coffee

Do you have vegetarian food?

Show desserts

What are your opening hours?

Do you have Wi-Fi?

Add Margherita Pizza

View cart

Checkout
```

---

# 📁 Data Sources

The chatbot is trained using:

- menu.csv
- faq.csv
- restaurant.csv

These files are converted into embeddings and indexed using FAISS.

---

# 🗄️ Database

SQLite stores:

- Orders
- Order Items

---

# 📈 Future Enhancements

- Voice Ordering
- Image-based Menu Search
- QR Code Ordering
- Online Payments
- Order Tracking
- Admin Dashboard
- Inventory Management
- Customer Login
- Recommendation Engine
- Multi-language Support
- WhatsApp Integration
- Table Reservation
- Live Kitchen Status

---

# 👨‍💻 Author

**Sugumar R**

AI Developer | Python | FastAPI | RAG | Machine Learning

GitHub:
https://github.com/theiniyanvlogs-lab

---

# ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is released under the MIT License.
