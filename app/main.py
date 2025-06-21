from fastapi import FastAPI
from app.routes import movimientos

app = FastAPI(title="API Presupuesto Personal")

app.include_router(movimientos.router, prefix="/movimientos", tags=["Movimientos"])
