from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import model

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def formulaire_get(request: Request):
    # Formulaire vide
    return templates.TemplateResponse("item.html", {"request": request, "commune": None, "meteo": None})

@app.post("/", response_class=HTMLResponse)
async def formulaire_post(request: Request, code_postal: str = Form(...)):
    commune = model.recup_commune(code_postal)
    meteo = None
    if commune:
        lat, lon = model.get_coords(commune)
        if lat and lon:
            meteo = model.get_meteo(lat, lon)

    return templates.TemplateResponse("item.html", {
        "request": request,
        "commune": commune,
        "meteo": meteo,
        "codePostal": code_postal  # <- ajoute ça pour passer le code postal au template
    })


