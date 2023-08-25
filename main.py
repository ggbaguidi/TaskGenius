"""Entry of my app"""
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root() -> dict:
    """
    Args: None
    Return:  dict(greatings)
    """
    return {"Home": "Welcome to TaskGenius"}