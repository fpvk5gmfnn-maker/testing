# AI Project Starter Guide for a Business Use Case

This guide walks through how to structure, build, and iterate on a small AI-powered product when you are new to the field. It favors simple, reliable tools so you can ship value quickly and learn as you go.

## 1) Clarify the Business Problem
- **Write one-sentence goal** (e.g., "Automatically summarize customer support emails into action items").
- **Define success metrics** such as response-time reduction, time saved per user, or conversion uplift.
- **Identify constraints**: data privacy rules (GDPR/CCPA), latency needs, and budget for hosting and APIs.

## 2) Collect and Organize Data
- **Start with small, real examples** (50–200 records) that reflect the end task.
- **Anonymize sensitive fields** before storing or sending to any model provider.
- **Label the data**: pair inputs (emails, tickets, documents) with desired outputs (summaries, categories, answers).
- **Store safely**: a simple CSV/JSON in a private repo or a secure database is enough for early prototypes.

## 3) Choose an Initial Model Strategy
- **API-first** for speed: use a hosted LLM (e.g., OpenAI API) to avoid managing infrastructure.
- **Prompting over training**: craft a clear system prompt, include examples, and set boundaries (tone, style, length).
- **Guardrails**: add instructions to decline unrelated requests and to keep outputs concise.

## 4) Build a Minimal Viable Product (MVP)
- **Backend**: a lightweight Python service (FastAPI) with a single endpoint that calls the model and returns results.
- **Frontend**: the included `app/templates/index.html` page shows a gradient-styled form that calls `/summaries` via fetch.
- **Logging**: store prompts, responses, and user feedback (thumbs up/down) to improve later.
- **Testing**: add smoke tests for the API route and a few golden responses to catch regressions.

## 5) Iterate with Prompt and Data Improvements
- **Collect failures**: save examples where the model is wrong or unhelpful.
- **Refine prompts**: add more examples, specify formatting, and set stricter instructions for edge cases.
- **Use retrieval** if needed: store your domain documents (policies, product info) in a vector database and pass the top results to the model so it stays grounded.

## 6) Consider Fine-Tuning (Optional)
- **When to do it**: you see repeatable errors that prompting cannot fix, and you have 500–2,000+ high-quality pairs.
- **How**: start with a small fine-tune on a cost-effective model; keep a held-out validation set to measure gains.
- **Deploy**: version models and prompts; route a small percentage of traffic to new versions before full rollout.

## 7) Operate Safely
- **Content filters**: block disallowed inputs/outputs (PII leakage, unsafe requests).
- **Rate limiting**: protect the service from abuse and control costs.
- **Monitoring**: track latency, error rates, and user satisfaction. Alert on spikes.
- **Compliance**: document data flows and vendor usage; provide opt-outs where required.

## 8) Simple Project Roadmap
- **Week 1**: finalize the problem statement, gather sample data, write initial prompt, and build one API endpoint.
- **Week 2**: add feedback logging, basic frontend, and golden tests. Start collecting real user feedback.
- **Week 3–4**: iterate on prompts, add retrieval if needed, and harden monitoring and security.

## 9) Lightweight Tech Stack Recommendation
- **Language**: Python 3.11+
- **Backend**: FastAPI + `httpx` for API calls
- **Model access**: Hosted LLM API (e.g., OpenAI) with API key in environment variables
- **Retrieval (optional)**: SQLite + `chromadb` or `faiss` for small-scale vector search
- **Testing**: `pytest` for unit tests; `ruff` for linting

## 10) Example One-Endpoint Starter
The repository now includes a ready-to-run FastAPI app with a styled frontend:

- Start the server with `uvicorn app.main:app --reload`.
- Visit `http://127.0.0.1:8000/` to see the gradient UI and test summaries.
- Update `app/summary.py` to call your preferred LLM API instead of the built-in heuristic summarizer.

### Example handler

```python
from fastapi import FastAPI

app = FastAPI()


def call_llm(prompt: str) -> str:
    # TODO: integrate an LLM API call here
    return f"Echo: {prompt}"


@app.post("/summaries")
def summarize(payload: dict):
    text = payload.get("text", "")
    result = call_llm(f"Summarize this for a busy manager: {text}")
    return {"summary": result}
```

## 11) Next Steps for You
- Pick one business problem and write its success metric today.
- Gather 20–50 real examples and draft a first prompt using them.
- Build the single-endpoint API (above) and try it with teammates before expanding.
- Add simple logging of inputs/outputs and a thumbs up/down field to capture feedback.

Use this as a checklist to stay focused on delivering measurable business value, not just model experimentation.
