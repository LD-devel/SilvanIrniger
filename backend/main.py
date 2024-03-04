from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 

from typing_extensions import Annotated
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.mount("/assets", StaticFiles(directory="../frontend/assets", html=True), name="static")
app.mount("/images", StaticFiles(directory="../frontend/images", html=True), name="static")
app.mount("/utils", StaticFiles(directory="../frontend/utils", html=True), name="static")

@app.get("/")
async def get_index():
    return FileResponse("../frontend/index.html")

@app.get("/about")
async def get_about():
    return FileResponse("../frontend/about.html")

@app.get("/concerts")
async def get_concerts():
    return FileResponse("../frontend/concerts.html")

@app.get("/contact")
async def get_contact():
    return FileResponse("../frontend/contact.html")

@app.get("/gallery")
async def get_gallery():
    return FileResponse("../frontend/gallery.html")

@app.post("/submit-contact-form/")
async def submit_form(name: Annotated[str, Form()],
                      email: Annotated[str, Form()],
                      subject: Annotated[str, Form()],
                      message: Annotated[str, Form()]): 
    try:
        return {"message": "Form submission successful "}
    except Exception as e:
        print("this step")
        raise HTTPException(status_code=500, detail="Internal server error")
