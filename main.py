from fastapi import FastAPI, Form
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Krishi Seva Server is live!"}

@app.post("/whatsapp")
async def whatsapp_reply(Body: str = Form(...)):
    print(f"[RECEIVED MESSAGE]: {Body}")

    # Create the TwiML response
    resp = MessagingResponse()
    resp.message(f'Namaste! Krishi Seva received your message: "{Body}"')

    # Twilio strictly requires 'application/xml'
    return PlainTextResponse(content=str(resp), media_type="application/xml")