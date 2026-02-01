from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Vowel Counter", version="v1")

class Health(BaseModel):
    ok: bool

class VowelCountResponse(BaseModel):
    input: str
    vowel_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/vowel-count", response_model=VowelCountResponse)
def vowel_count(text: str = Query(..., description="Text to count vowels for")):
    matches = re.findall(r"[AEIOUaeiou]", text)
    return {"input": text, "vowel_count": len(matches)}
