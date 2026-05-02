import json
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

DATA_FILE = Path("static/daily_item.json")
DAILY_DATA = {}
try: 
    if DATA_FILE.exists():
        with open(DATA_FILE, mode='r', encoding='utf-8') as f:
            contents = f.read()
            DAILY_DATA = json.loads(contents)
    else:
        print("Fichier JSON introuvable au démarrage")
except  Exception as e:
    print(f"Erreur lors du chargement des données : {e}")

@app.get("/daily-item")
async def get_daily_item():
    if not DAILY_DATA:
        raise HTTPException(status_code=404, detail="Pas d'item")
    
    return {
        "title": DAILY_DATA.get("title"),
        "images": DAILY_DATA.get("image_url"),
        "description": DAILY_DATA.get("description"),
        "location": DAILY_DATA.get("location")
    }

@app.get("/check-price")
async def check_price(guess: float):
    if not DAILY_DATA or "price" not in DAILY_DATA:
        raise HTTPException(status_code=500, detail="Prix non configuré sur le serveur")
    
    try:
        actual_price = float(DAILY_DATA.get("price"))
    except ValueError:
        raise HTTPException(status_code=500, detail="Prix mal formaté sur le serveur")
    
    if guess < actual_price:
        return {"result": "LOW"}
    elif guess > actual_price:
        return {"result": "HIGH"}
    else:
        return {"result": "WIN"}