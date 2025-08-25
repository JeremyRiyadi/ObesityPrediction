from fastapi import FastAPI
import joblib
from pydantic import BaseModel
from typing import Literal
import pandas as pd

app = FastAPI()
model = joblib.load('pickle.pkl')

@app.get("/")
def read_root():
    return {"message" : "Welcome to Our Obesity Prediction Page"}

class Features(BaseModel):
    Gender : Literal['Male', 'Female']
    Age : int
    Height : float
    Weight : float
    family_history_with_overweight : Literal['yes', 'no']
    FAVC : Literal['yes', 'no']
    FCVC : float
    NCP : float
    CAEC : Literal['Always', 'Frequently', 'Sometimes', 'no']
    SMOKE : Literal['yes', 'no']
    CH2O : float
    SCC : Literal['yes', 'no']
    FAF : float
    TUE : float
    CALC : Literal['Always', 'Frequently', 'Sometimes', 'no']
    MTRANS : Literal['Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking']

@app.post('/predict')
def predict(data : Features) :
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {'Prediction': prediction[0]}