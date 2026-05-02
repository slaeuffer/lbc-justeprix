import json, aiofiles
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

DATA_FILE = Path("static/daily_item.json")

@app.get("/daily-item")
async def get_daily_item():
    if not DATA_FILE.exists():
        raise HTTPException(status_code=404, detail="Pas d'item")
    
    async with aiofiles.open(DATA_FILE, mode='r', encoding='utf-8') as f:
        contents = await f.read()
        item = json.loads(contents)
    
    print(item.get("title"))
    print(item.get("title"))
    print(item.get("title"))
    print(item.get("title"))
    print(item.get("title"))
    print(item.get("title"))
    return {
        "title": item.get("title"),
        "images": item.get("image_url"),
        "description": item.get("description"),
        "location": item.get("location")
    }

