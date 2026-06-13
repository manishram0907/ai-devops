from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "AI DevOps Assignment Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }