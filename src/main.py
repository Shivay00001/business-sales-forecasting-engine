from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
import io
from src.forecasting.engine import SalesForecaster

app = FastAPI(title="Sales Forecasting API")
forecaster = SalesForecaster()

class ForecastRequest(BaseModel):
    periods: int = 30

@app.post("/train")
async def train_model(file: UploadFile = File(...)):
    try:
        content = await file.read()
        df = pd.read_csv(io.BytesIO(content))
        # Ensure correct column names or map them
        if 'date' in df.columns and 'sales' in df.columns:
            df = df.rename(columns={'date': 'ds', 'sales': 'y'})
        
        forecaster.fit(df)
        return {"status": "success", "message": "Model trained successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/forecast")
async def get_forecast(request: ForecastRequest):
    try:
        forecast_df = forecaster.predict(periods=request.periods)
        # return only relevant columns for the projection
        result = forecast_df[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(request.periods).to_dict(orient='records')
        return {"forecast": result}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "ok", "engine": "Prophet"}
