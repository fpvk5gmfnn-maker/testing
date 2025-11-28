import re
from typing import List


def _split_sentences(text: str) -> List[str]:
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [sentence.strip() for sentence in parts if sentence.strip()]


def _top_sentences(sentences: List[str], max_sentences: int = 3) -> List[str]:
    return sentences[:max_sentences]


def generate_summary(text: str) -> str:
    """Create a concise, readable summary using simple heuristics.

    This keeps the app dependency-light while still returning useful output for demos.
    """
    normalized = text.strip()
    if not normalized:
        return ""

    sentences = _split_sentences(normalized)
    if not sentences:
        return normalized[:180]

    if len(sentences) == 1:
        return sentences[0][:240]

    selected = _top_sentences(sentences, max_sentences=2)
    summary = " ".join(selected)

    if len(summary) > 280:
        summary = summary[:277] + "..."

    return summary
