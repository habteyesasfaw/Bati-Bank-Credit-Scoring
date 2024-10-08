from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the request body schema
class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float
    # add more features as per your model

# Define the /predict endpoint
@app.post("/predict")
def predict(request: PredictionRequest):
    # For now, just return a dummy prediction. Replace with your actual model logic.
    prediction = 0.85  # This should be your model's prediction
    return {"prediction": prediction}
