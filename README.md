# 🍳 Become-A-Cook AI

<p align="center">
  <strong>AI Recipe Guessing Game with Chef-Level Evaluation Engine</strong>
</p>

<p align="center">
A full-stack AI-powered cooking challenge platform where users analyze dish images, reconstruct recipes, and receive brutally honest feedback from a Michelin-style AI Chef powered by Google Gemini.
</p>

<p align="center">
  <strong>Mode:</strong> 🎮 Game + 🤖 AI Evaluation Engine
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-16-black?logo=next.js" />
  <img src="https://img.shields.io/badge/FastAPI-Python-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/Google_Gemini-AI-8E75B2?logo=google" />
  <img src="https://img.shields.io/badge/PostgreSQL/Data-JSON-orange" />
</p>

---

# 📌 Overview

**Become-A-Cook AI** is an interactive AI cooking challenge platform where users attempt to reverse-engineer recipes from images and hints.

The system evaluates:
- Ingredient accuracy
- Cooking logic
- Step-by-step reasoning
- Hint usage efficiency

Then returns a **chef-style score + brutally honest feedback** powered by Gemini AI.

---

# 🍽️ Core Features

## 🎮 AI Cooking Game Engine

- Guess recipes from dish images and hints
- Step-by-step cooking plan submission
- Score-based evaluation system (0–100)
- Hint penalty system (-6 points per hint)
- Replayable challenges

---

## 🤖 AI Chef Evaluation System

- Gemini-powered reasoning engine
- Structured feedback generation:
  - 🔥 Roast (critique)
  - 👨‍🍳 Cooking feedback
  - 💡 Chef secret tips
- Ingredient matching engine
- Smart scoring algorithm

---

## 📚 Recipe Intelligence Layer

- 500+ recipe dataset (MealDB sourced)
- Category-based search system
- Recipe metadata extraction
- Ingredient normalization engine

---

## ⚡ Full-Stack Architecture

- FastAPI backend (high-performance API layer)
- Next.js frontend (game UI + interaction layer)
- JSON-based dataset (lightweight, fast queries)
- Modular service-based backend design

---

# 🧠 System Architecture

```text
Frontend (Next.js UI)
        │
        ▼
FastAPI Backend (Game Engine)
        │
 ┌──────┼──────────────┐
 ▼      ▼              ▼
Recipes  AI Engine   Validation Layer
(JSON)   (Gemini)    (Pydantic)
        │
        ▼
   Score + Feedback Response
---

# 🚀 Quick Start

### 📦 Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **Gemini API Key** (optional but recommended)

### 1️⃣ Clone Project
```bash
git clone <your-repo-url>
cd python-recipe
```

### 2️⃣ Backend Setup (FastAPI)
```bash
python3 -m venv backend/venv
backend/venv/bin/pip install -r backend/requirements.txt
```

**Start Backend**
```bash
backend/venv/bin/python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Backend: http://localhost:8000
Swagger Docs: http://localhost:8000/docs

### 3️⃣ Frontend Setup (Next.js)
```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:3000

### 4️⃣ Run Full App
Make sure both servers are running:
- **Backend** → 8000
- **Frontend** → 3000

---

# 🗂️ Project Structure
```text
python-recipe/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── data/recipes.json
│   ├── scripts/
│   └── app/
│       ├── database/
│       ├── models/
│       ├── routes/
│       └── services/
│
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── components/
│   │   └── lib/
│   └── package.json
```

---

# 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Next.js 16, React 19, TypeScript |
| **Backend** | FastAPI (Python) |
| **AI Engine** | Google Gemini |
| **Data Layer** | JSON (500+ recipes) |
| **Validation** | Pydantic v2 |
| **Server** | Uvicorn |

---

# 📡 API Reference

**Base URL**
`http://localhost:8000`

### 🔍 Search Recipes
`GET /recipes/search?q=&page=1&limit=12`

### 🍽️ Get Recipe
`GET /recipes/{id}`

### 🤖 AI Evaluation
`POST /recipes/validate`

**Request**
```json
{
  "recipe_id": 1,
  "plan": "I will marinate chicken in yogurt and spices...",
  "hints_used": 2
}
```

**Response**
```json
{
  "score": 78,
  "feedback": "🔥 THE ROAST: ... 👨‍🍳 THE CRITIQUE: ... 💡 CHEF SECRET: ...",
  "matched_ingredients": ["Chicken", "Yogurt"],
  "all_ingredients": ["Chicken", "Rice", "Yogurt", "Onion"]
}
```

---

# 🔄 Dataset Regeneration
```bash
backend/venv/bin/python backend/scripts/import_recipes.py
```

---

# 🧠 Engineering Highlights
- AI-driven scoring system (Gemini reasoning engine)
- Ingredient matching algorithm
- Hint penalty-based gamification system
- Clean FastAPI modular architecture
- Lightweight JSON-based dataset design
- Full-stack separation of concerns

---

# 🎯 Game Mechanics
- **Max Score:** 100
- **Each hint:** -6 points
- **Perfect score =** no hints + full ingredient match
- **AI Chef is intentionally strict** (no mercy 🍳)

---

# 🔮 Future Improvements
- PostgreSQL migration for scalability
- Image-based recipe detection (Vision AI)
- Multiplayer cooking challenges
- Leaderboard system
- User accounts & progression system
- Daily cooking challenges

---

# 📝 License

MIT License