# 🚀 AI Branding Assistant (Groq Powered)

It provides instant brand names, marketing content, color palettes, taglines, and branding guidance through a clean FastAPI backend and a modern glass-style UI.

This version uses **Groq only** — simple, fast, and easy to run locally.

---

# ✨ Features

- ✅ Brand name generation
- ✅ Tagline creation
- ✅ Marketing content writing
- ✅ Brand color palette suggestions
- ✅ Sentiment analysis + rewrite
- ✅ Logo prompt generator (for image tools)
- ✅ AI branding assistant chat
- ✅ Modern gradient + glass UI
- ✅ FastAPI backend
- ✅ Groq LLaMA text generation

---

# 🧠 AI Stack

| Component | Model |
|-----------|---------|
Text Generation | Groq LLaMA-3.3-70B |
Backend | FastAPI |
Frontend | HTML + CSS + JavaScript |
Server | Uvicorn |

---

# 📁 Project Structure

```text
bizforge-lite/
│
├── main.py
├── config.py
├── requirements.txt
├── .env
│
├── services/
│   └── groq_service.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── app.js
```

---

# ⚙️ Setup Instructions

## 1️⃣ Install Python

Python 3.10+ required  
https://python.org

---

## 2️⃣ Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Get Groq API Key

1. Go to: https://console.groq.com
2. Create account
3. Generate API key
4. Copy key

---

## 5️⃣ Create `.env` File

```env
GROQ_API_KEY=your_key_here
```

---

# ▶️ Run the App

```bash
python -m uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

# 🧪 API Endpoints

| Endpoint | Function |
|------------|----------------|
/api/brand | Generate brand names |
/api/tagline | Generate taglines |
/api/content | Marketing content |
/api/colors | Color palette |
/api/sentiment | Sentiment analysis |
/api/logo_prompt | Logo prompt |
/api/chat | Branding assistant chat |
/health | Server health |

---

# 💡 Example Prompts

**Brand Names**
> Smart AI clothing startup — modern tone

**Marketing Content**
> Eco-friendly premium coffee brand

**Chat**
> Help me position my SaaS product

---

# 🎯 Use Cases

- Startup brand ideation
- Product launch prep
- Marketing draft creation
- Naming brainstorm
- Visual identity planning
- Portfolio AI project demo

---

# 🚀 Future Enhancements

- Logo image generation
- Downloadable brand kit PDF
- Multi-page dashboard
- User history
- SaaS deployment
- Affiliate product linking

---

# 🛠 Troubleshooting

## uvicorn not recognized

Run:

```bash
python -m uvicorn main:app --reload
```

---

## API key errors

Check `.env` file exists and key is valid.

---

# 📜 License

MIT — Free to use and modify.

---

# 👤 Author

Built as an AI branding automation project using Groq + FastAPI.

---

# ⭐ If This Helped

Star the repo and build your own AI SaaS tools 🚀
