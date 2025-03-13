import csv
from pydantic import BaseModel  # type: ignore
from typing import List, Optional
from datetime import date

class HistoriaClinica(BaseModel):
    id: int
    nombre: str
    edad: int
    genero: str
    tSangre: str
    alergias: list
    cMedicas: list
    

