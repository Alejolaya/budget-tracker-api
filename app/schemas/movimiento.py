from pydantic import BaseModel
from datetime import datetime

class MovimientoCreate(BaseModel):
    tipo: str
    descripcion: str
    monto: float

class MovimientoOut(MovimientoCreate):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
