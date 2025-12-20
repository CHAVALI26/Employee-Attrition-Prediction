from fastapi import FastAPI
import pandas as pd
import joblib

from api.schema import EmployeeInput, PredictionResponse
from src.feature_engineering import FeatureEngineer
from src.preprocessing import DataPreprocessor

# Initialize FastAPI app
app = FastAPI( title="Employee Attrition Prediction API",version ="1.0")

# Load trained model
model = joblib.load("models/xgboost_attrition_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

#Feature engineer
fe= FeatureEngineer()

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict", response_model=PredictionResponse)
def predict_attrition(data: EmployeeInput):
    # Convert input to DataFrame
    df = pd.DataFrame([data.dict])

    # Feature engineering
    df_fe = fe.engineer_features(df)

    # Preprocessing (NO fitting, only transform)
    X = preprocessor.preprocessor.transform(df_fe.drop(columns=["Attrition"],error="ignore"))

    #prediction
    attrition_prob = model.predict_proba(X)[:,1][0]

    return { "attrition_probability": round(float(attrition_prob),4) }