from pydantic import BaseModel  # type: ignore
from typing import List, Optional
from datetime import date

class HistoriaClinica(BaseModel):
    id: int
    diagnostico: str
    tratamiento: str
    fecha: date

