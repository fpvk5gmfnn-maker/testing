# AI Project Starter

A small FastAPI app that summarizes text with a styled frontend. Use it as a starting point to plug in your preferred LLM API.

## Quickstart

1) Create and activate a virtual environment (optional):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies:

```bash
pip install -r requirements.txt
```

3) Run the app:

```bash
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/ in your browser and paste text to summarize.

### Environment note

`pytest` is already available in the environment used for these examples. If you run into proxy issues installing other packages (e.g., `fastapi`), try using an existing virtual environment with the dependencies preinstalled or configure your proxy settings before rerunning `pip install -r requirements.txt`.

## Testing

```bash
pytest
```

## Project structure

- `app/main.py`: FastAPI app wiring routes, templates, and static assets.
- `app/summary.py`: Lightweight summarization helper; replace with your LLM call when ready.
- `app/templates/index.html`: Styled landing page with a fetch-based form.
- `app/static/style.css`: Gradient, typography, and layout styles.
- `tests/`: Basic API and helper tests.
- `docs/AI_PROJECT_GUIDE.md`: Beginner-friendly roadmap for shipping an AI-powered product.
