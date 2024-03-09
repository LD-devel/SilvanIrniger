from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi.responses import RedirectResponse

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

@app.get("/success")
async def get_success():
    return RedirectResponse("/")

@app.post("/success")
async def post_success():
    return FileResponse("../frontend/contact_success.html")

@app.post("/submit-contact-form/")
async def submit_form(name: Annotated[str, Form()],
                      email: Annotated[str, Form()],
                      subject: Annotated[str, Form()],
                      message: Annotated[str, Form()]): 
    try:
        return RedirectResponse("/success")
    except:
        raise HTTPException(status_code=500, detail="Internal server error")

