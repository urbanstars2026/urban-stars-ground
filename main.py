from fastapi import FastAPI, Query

app = FastAPI()

VERIFY_TOKEN = "Arjun@2026"

@app.get("/webhook")
def verify(
    hub_mode: str = Query(..., alias="hub.mode"),
    hub_challenge: str = Query(..., alias="hub.challenge"),
    hub_verify_token: str = Query(..., alias="hub.verify_token")
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)  # WhatsApp expects exact value
    return "Verification failed"

@app.get("/")
def health():
    return {"status": "running"}
