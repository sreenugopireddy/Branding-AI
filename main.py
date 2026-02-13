from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.groq_service import ask_groq

# -----------------------------
# FastAPI App Init
# -----------------------------

app = FastAPI(title="BizForge Lite")

# CORS (safe for local dev + frontend JS fetch)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# -----------------------------
# Request Models
# -----------------------------

class BrandReq(BaseModel):
    idea: str
    tone: str


class ContentReq(BaseModel):
    desc: str
    tone: str


class ColorReq(BaseModel):
    industry: str
    tone: str


class TextReq(BaseModel):
    text: str


class NameReq(BaseModel):
    name: str


class LogoReq(BaseModel):
    name: str
    industry: str


class ChatReq(BaseModel):
    msg: str


# -----------------------------
# Frontend Route
# -----------------------------

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


# -----------------------------
# API — Brand Name Generator
# -----------------------------

@app.post("/api/brand")
def generate_brand(data: BrandReq):

    prompt = f"""
Generate 12 creative brand names.

Business idea: {data.idea}
Tone: {data.tone}

Return only a clean bullet list.
"""

    result = ask_groq(prompt)
    return JSONResponse({"result": result})


# -----------------------------
# API — Taglines
# -----------------------------

@app.post("/api/tagline")
def generate_tagline(data: NameReq):

    prompt = f"Generate 5 catchy brand taglines for {data.name}"

    return {"result": ask_groq(prompt)}


# -----------------------------
# API — Marketing Content
# -----------------------------

@app.post("/api/content")
def generate_content(data: ContentReq):

    prompt = f"""
Write professional marketing content.

Description: {data.desc}
Tone: {data.tone}

Include:
- short version
- long version
- bullet benefits
"""

    return {"result": ask_groq(prompt)}


# -----------------------------
# API — Color Palette
# -----------------------------

@app.post("/api/colors")
def generate_colors(data: ColorReq):

    prompt = f"""
Suggest a brand color palette.

Industry: {data.industry}
Tone: {data.tone}

Return 5 HEX colors with meaning.
"""

    return {"result": ask_groq(prompt)}


# -----------------------------
# API — Sentiment Analysis
# -----------------------------

@app.post("/api/sentiment")
def sentiment(data: TextReq):

    prompt = f"""
Analyze sentiment of this text.
Classify + explain + rewrite better:

Text:
{data.text}
"""

    return {"result": ask_groq(prompt)}


# -----------------------------
# API — Logo Prompt Generator
# -----------------------------

@app.post("/api/logo_prompt")
def logo_prompt(data: LogoReq):

    prompt = f"""
Create a professional AI image prompt for a logo.

Brand: {data.name}
Industry: {data.industry}

Include:
style, color, icon idea, mood, layout.
"""

    return {"result": ask_groq(prompt)}


# -----------------------------
# API — Branding Chatbot
# -----------------------------

@app.post("/api/chat")
def chat(data: ChatReq):

    return {"result": ask_groq(data.msg)}


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
def health():
    return {"status": "ok", "service": "BizForge Lite"}

