from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "Arjun@2026")

@app.get("/")
def health():
    return {"status": "running"}

# Webhook verification
@app.get("/webhook")
def verify(hub_mode: str, hub_challenge: int, hub_verify_token: str):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return hub_challenge
    return "Verification failed"

# Receive messages
@app.post("/webhook")
async def receive_message(req: Request):
    data = await req.json()
    print("Incoming:", data)
    return {"status": "ok"}
