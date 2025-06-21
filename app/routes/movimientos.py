from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Movimiento
from app.schemas.movimiento import MovimientoCreate, MovimientoOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MovimientoOut)
def crear_movimiento(movimiento: MovimientoCreate, db: Session = Depends(get_db)):
    nuevo = Movimiento(**movimiento.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/", response_model=list[MovimientoOut])
def listar_movimientos(db: Session = Depends(get_db)):
    return db.query(Movimiento).all()
