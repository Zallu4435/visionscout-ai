# 🍳 Become-A-Cook AI

An AI-powered recipe guessing game where you analyze dish images, decode hints, and describe the cooking method — then get brutally honest feedback from a Michelin-star Chef AI.

---

## 🚀 How to Start

### Prerequisites

- **Python 3.10+** — [Download](https://python.org)
- **Node.js 18+** — [Download](https://nodejs.org)
- **Gemini API Key** — [Get one free](https://aistudio.google.com/app/apikey)

---

### 1. Clone & Setup Environment

```bash
git clone <your-repo-url>
cd python-recipe
```

Create a `.env` file in the **project root**:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 2. Start the Backend (FastAPI)

> ⚠️ Always run from the **project root** (`python-recipe/`), not from inside `backend/`.

```bash
# First time only — create the virtual environment and install dependencies
python3 -m venv backend/venv
backend/venv/bin/pip install -r backend/requirements.txt

# Start the server
backend/venv/bin/python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

Backend runs at → **http://localhost:8000**  
API docs (Swagger) → **http://localhost:8000/docs**

---

### 3. Start the Frontend (Next.js)

```bash
cd frontend
npm install       # First time only
npm run dev
```

Frontend runs at → **http://localhost:3000**

---

### 4. Open the App

Visit **http://localhost:3000** in your browser. Both servers must be running simultaneously.

---

## 🗂️ Project Structure

```
python-recipe/
├── .env                        # API keys (never commit this)
├── .gitignore
├── README.md
│
├── backend/
│   ├── main.py                 # FastAPI app entry point
│   ├── requirements.txt        # Python dependencies
│   ├── venv/                   # Python virtual environment (gitignored)
│   ├── data/
│   │   └── recipes.json        # 500 recipe dataset
│   ├── scripts/
│   │   ├── generate_recipes.py # Seed script (50 base recipes)
│   │   ├── import_recipes.py   # Fetches 500 recipes from MealDB API
│   │   └── list_models.py      # Debug: lists available Gemini models
│   └── app/
│       ├── __init__.py
│       ├── database/
│       │   ├── __init__.py
│       │   └── db.py           # JSON data loader & query functions
│       ├── models/
│       │   ├── __init__.py
│       │   └── schemas.py      # Pydantic request/response models
│       ├── routes/
│       │   ├── __init__.py
│       │   └── recipes.py      # API route definitions
│       └── services/
│           ├── __init__.py
│           └── recipe_service.py  # Business logic + Gemini AI integration
│
└── frontend/
    ├── package.json
    └── src/
        ├── app/
        │   ├── globals.css         # Global design system & styles
        │   ├── layout.tsx
        │   ├── page.tsx            # Home page
        │   ├── search/
        │   │   └── page.tsx        # Recipe search & browse
        │   └── recipe/[id]/
        │       └── page.tsx        # Recipe detail & game page
        ├── components/
        │   ├── Navbar.tsx
        │   ├── Footer.tsx
        │   ├── RecipeCard.tsx
        │   ├── SearchBar.tsx
        │   ├── Pagination.tsx
        │   └── Loading.tsx
        └── lib/
            └── config.ts           # API base URL config
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 16, React 19, TypeScript |
| **Styling** | Vanilla CSS (custom design system) |
| **Icons** | Lucide React |
| **Backend** | FastAPI, Python 3.14 |
| **Server** | Uvicorn (ASGI) |
| **AI** | Google Gemini (`gemini-flash-latest`) |
| **Data** | JSON flat-file (500 recipes from MealDB) |
| **Validation** | Pydantic v2 |

---

## 📡 API Reference

Base URL: `http://localhost:8000`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/recipes/search?q=&page=1&limit=12&category=` | Search & paginate recipes |
| `GET` | `/recipes/{id}` | Get recipe details + hints |
| `POST` | `/recipes/validate` | Submit cooking plan for AI scoring |

### POST `/recipes/validate` — Request Body

```json
{
  "recipe_id": 1,
  "plan": "I would start by marinating the chicken in yogurt...",
  "hints_used": 2
}
```

### Response

```json
{
  "score": 78,
  "feedback": "🔥 THE ROAST: ...\n👨‍🍳 THE CRITIQUE: ...\n💡 THE CHEF'S SECRET: ...",
  "matched_ingredients": ["Chicken", "Yogurt"],
  "all_ingredients": ["Chicken", "Basmati Rice", "Yogurt", "Onion"]
}
```

---

## 🔄 Regenerate Recipe Dataset

If you want to rebuild the `recipes.json` from scratch:

```bash
# Fetch 500 real recipes from TheMealDB (free API, no key needed)
cd python-recipe
backend/venv/bin/python backend/scripts/import_recipes.py
```

---

## 🔑 Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | ✅ Yes | Google Gemini API key for AI feedback |

> Without the key, the app still works — AI feedback is replaced with an offline message and scoring still functions normally.

---

## 💡 Tips

- **Hints cost `-6 pts` each** from your maximum potential score of 100
- **Zero hints + all ingredients = perfect 100** guaranteed
- The AI Chef persona is intentionally brutal — don't take it personally 🍳
- Run the backend from the **project root**, not from `backend/` — module imports depend on it
