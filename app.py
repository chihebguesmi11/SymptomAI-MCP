from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio
from client import run_symptom_analysis  # your robust client
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def analyze(request: Request, user_input: str = Form(...)):
    # Run MCP client
    try:
        symptoms_text, details_text, diseases_text, advice_text = await run_symptom_analysis(user_input)
    except Exception as e:
        symptoms_text = details_text = diseases_text = advice_text = f"Error: {e}"

    result = {
        "symptoms": symptoms_text or "No symptoms extracted.",
        "details": details_text or "No details extracted.",
        "diseases": diseases_text or "No diseases found.",
        "advice": advice_text or "No advice available."
    }

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result, "user_input": user_input}
    )
