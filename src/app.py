import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    app_id = os.getenv("HOSTNAME", "App não identificado!!!")
    
    html_path = Path(__file__).parent / "templates/index.html"
    html_content = html_path.read_text()
    html_content = html_content.replace("{{APP_ID}}", app_id)
    
    return HTMLResponse(content=html_content)