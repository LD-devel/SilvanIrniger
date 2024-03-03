from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 

from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.mount("/", StaticFiles(directory="../frontend", html=True), name="static")

class ContactForm(BaseModel):
    name: str
    email: str
    subject: str
    message: Optional[str] = None

@app.post("/submit-contact-form/")
async def submit_form(contact_form: ContactForm):
    try:
        return {"message": "Form submission successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

