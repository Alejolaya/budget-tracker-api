# Etapa 1: Construcción
FROM python:3.11-slim AS builder

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Crear directorios
WORKDIR /app

# Instalar dependencias del sistema (opcional: mejorar seguridad y compatibilidad)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc curl && \
    rm -rf /var/lib/apt/lists/*

# Copiar dependencias
COPY requirements.txt .

# Crear entorno virtual y preinstalar dependencias
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Etapa 2: Imagen final liviana
FROM python:3.11-slim

WORKDIR /app

# Copiar desde la etapa anterior
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

# Copiar el código fuente
COPY app ./app

# Puerto por defecto de FastAPI (puedes cambiarlo)
EXPOSE 8000

# Comando de arranque
# CMD ["python", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "app/startup.py"]
