import pandas as pd
from fastapi import FastAPI
from mangum import Mangum
from app.api.v1.api import router as api_router
from app.api.v1.endpoints.images import data

app = FastAPI()


@app.on_event('startup')
def init_data():
    df = pd.read_csv('images.csv')
    data["df"] = df


@app.get("/healthcheck")
async def health_check():
    return {"message": "OK"}


app.include_router(api_router, prefix="/api/v1")

handler = Mangum(app)