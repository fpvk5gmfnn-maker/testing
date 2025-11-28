from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from .summary import generate_summary

app = FastAPI(title="AI Project Starter", version="1.0.0")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to summarize")


class SummarizeResponse(BaseModel):
    summary: str
    original_length: int
    reduced_length: int


@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """Serve a simple, styled landing page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/summaries", response_model=SummarizeResponse)
async def create_summary(payload: SummarizeRequest) -> SummarizeResponse:
    """Generate a concise summary from user-provided text."""
    summary = generate_summary(payload.text)

    if not summary:
        raise HTTPException(status_code=400, detail="Unable to summarize the provided text.")

    return SummarizeResponse(
        summary=summary,
        original_length=len(payload.text),
        reduced_length=len(summary),
    )


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
