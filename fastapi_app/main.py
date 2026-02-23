import psutil
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from loguru import logger
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Gauge, generate_latest
from starlette.responses import Response

load_dotenv()
app = FastAPI()

# Monitoring
REQUEST_COUNT = Counter("app_requests_total", "Total requests", ["method", "endpoint"])
CPU_USAGE = Gauge("system_cpu_usage", "Usage CPU")

logger.add("/logs/fastapi.log", rotation="500 MB")

@app.get("/")
async def root():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return {"status": "up"}

@app.post("/predict")
async def predict(data: str = Form(...)):
    logger.info(f"Donnée reçue : {data}")
    return {"prediction": "Valeur prédite", "value": 450}

@app.get("/metrics")
async def metrics():
    CPU_USAGE.set(psutil.cpu_percent())
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)