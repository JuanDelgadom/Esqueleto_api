from fastapi import APIRouter, HTTPException
from src.models.paciente import Paciente
from src.models.historiaClinica import HistoriaClinica
from faker import Faker
import random

router = APIRouter()

pacientes_db = [Paciente.crear_paciente_aleatorio(i + 1) for i in range(100)]

@router.get("/pacientes/", response_model=list[Paciente])
async def obtener_todos_los_pacientes():
    return pacientes_db

@router.get("/pacientes/{id_paciente}", response_model=Paciente)
async def obtener_paciente_por_id(id_paciente: int):
    paciente = next((p for p in pacientes_db if p.id == id_paciente), None)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.post("/pacientes/crear_aleatorios/{cantidad}")
async def crear_pacientes_aleatorios(cantidad: int):
    nuevos_pacientes = [
        Paciente.crear_paciente_aleatorio(len(pacientes_db) + i + 1)
        for i in range(cantidad)
    ]
    pacientes_db.extend(nuevos_pacientes)
    return {
        "mensaje": f"{cantidad} pacientes creados exitosamente",
        "pacientes": nuevos_pacientes
    }

@router.get("/historias/")
async def obtener_todas_las_historias():
    historiasClinica = []
    for p in pacientes_db:
        historiasClinica.append(p.historial_clinico)
    return historiasClinica

@router.get("/historia/{id_paciente}", response_model=list)
async def obtener_historia_por_id(id_paciente: int):
    paciente = next((p for p in pacientes_db if p.id == id_paciente), None)
    if paciente is None:
        raise HTTPException(status_code=404, detail="Historia clínica no encontrada")
    return paciente.historial_clinico