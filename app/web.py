import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from .agents import DocstringAgent, ReadmeAgent

app = FastAPI(title="AI Documentation Agent")

# Mount static folder (VERY IMPORTANT for CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# =========================
# Home Page
# =========================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": None}
    )


# =========================
# Generate Docstrings
# =========================
@app.post("/generate-docstring", response_class=HTMLResponse)
async def generate_docstring(request: Request, file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    agent = DocstringAgent()
    agent.generate(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        updated_code = f.read()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": updated_code
        }
    )


# =========================
# Generate README
# =========================
@app.post("/generate-readme", response_class=HTMLResponse)
async def generate_readme(request: Request, folder_path: str = Form(...)):

    agent = ReadmeAgent()
    agent.generate(folder_path)

    readme_path = os.path.join(folder_path, "README.md")

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = "README could not be generated."

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": content
        }
    )

