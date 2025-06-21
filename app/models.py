from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Movimiento(Base):
    __tablename__ = "movimientos"
    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)  # ingreso/gasto
    descripcion = Column(String)
    monto = Column(Float)
    fecha = Column(DateTime, default=datetime.datetime.utcnow)
