import json
import os
from fastapi import APIRouter, HTTPException
from src.models.historiaClinica import HistoriaClinica

router = APIRouter()

historias_clinicas_db = []

def cargar_datos():
    global historias_clinicas_db
    try:
        ruta_datos = os.path.join(os.path.dirname(__file__), '..', '..', 'Datos', 'datos.json')
        with open(ruta_datos, "r", encoding="utf-8") as file:
            datos = json.load(file)
            historias_clinicas_db = [HistoriaClinica(**item) for item in datos]
    except FileNotFoundError:
        print("Error: El archivo 'historias_clinicas.json' no fue encontrado.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON tiene un formato incorrecto.")

cargar_datos()


@router.get("/historias/")
async def obtener_todas_las_historias():
    return historias_clinicas_db

@router.get("/historia/{id}", response_model=HistoriaClinica)
async def obtener_historia_por_id(id: int):
    historia = next((h for h in historias_clinicas_db if h.id == id), None)
    if historia is None:
        raise HTTPException(status_code=404, detail="Historia clínica no encontrada")
    return historia