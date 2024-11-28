from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from config.db import get_db
from models.note import Note

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    db = get_db()
    docs = db.notes.find({})

    newDocs = [{"title": doc.get("title"), "desc": doc.get("desc", "No Description")} for doc in docs]
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/add")
async def add_note(request: Request, title: str = Form(...), desc: str = Form(...)):

    db= get_db()
    db.notes.insert_one({"title": title, "desc": desc})
    
    # Redirect to the index page after adding the note
    return RedirectResponse(url="/", status_code=303)