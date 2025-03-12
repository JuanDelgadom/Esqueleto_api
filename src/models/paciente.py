from pydantic import BaseModel
from typing import List, Optional
from datetime import date
from faker import Faker
from src.models.historiaClinica import HistoriaClinica

fake = Faker()

class Paciente(BaseModel):
    id: int
    nombre: str
    edad: int
    genero: str
    historial_clinico: List[HistoriaClinica]

    @staticmethod
    def crear_paciente_aleatorio(id: int) -> "Paciente":
        return Paciente(
            id=id,
            nombre=fake.name(),
            edad=fake.random_int(min=0, max=100),
            genero=fake.random_element(elements=["Masculino", "Femenino"]),
            historial_clinico=[
                HistoriaClinica(
                    id=fake.random_int(min=1000, max=9999),
                    diagnostico=fake.sentence(nb_words=6),
                    tratamiento=fake.sentence(nb_words=8),
                    fecha=fake.date_this_decade().strftime('%Y-%m-%d')
                ) for _ in range(fake.random_int(min=1, max=5))
            ]
        )