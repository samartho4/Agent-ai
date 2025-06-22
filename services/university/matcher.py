"""Program matching against EduCanada data."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, List

import httpx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "programs.json"
EDUCANADA_URL = os.getenv("EDUCANADA_URL")


def load_programs() -> List[dict[str, Any]]:
    """Return program data from a remote EduCanada source if available."""
    if EDUCANADA_URL:
        try:
            resp = httpx.get(EDUCANADA_URL, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if isinstance(data, list):
                return data
        except Exception:
            pass
    with DATA_PATH.open() as f:
        return json.load(f)




def find_matches(profile: dict[str, Any], limit: int = 3) -> List[dict[str, Any]]:
    """Return top program matches for the given profile using cosine similarity."""
    desired = profile.get("program", "")
    programs = load_programs()
    corpus = [p["program"] for p in programs]
    vectorizer = TfidfVectorizer().fit(corpus + [desired])
    program_vecs = vectorizer.transform(corpus)
    query_vec = vectorizer.transform([desired])
    sims = cosine_similarity(query_vec, program_vecs)[0]
    scored = list(zip(sims, programs))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in scored[:limit]]
