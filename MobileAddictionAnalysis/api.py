from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

class UserInput(BaseModel):
    screen_time: float
    social_media: float
    phone_checks: int
    usage_before_sleep: float
    usage_after_waking: int
    gaming_time: float
    interruption: int

@app.post("/predict")
def predict_addiction(data: UserInput):
    features = np.array([[
        data.screen_time,
        data.social_media,
        data.phone_checks,
        data.usage_before_sleep,
        data.usage_after_waking,
        data.gaming_time,
        data.interruption
    ]])

    prediction = model.predict(features)[0]
    level = int(prediction)

    levels_map = {
        0: "Low Addiction",
        1: "Moderate Addiction",
        2: "High Addiction"
    }

    return {
        "prediction": levels_map.get(level, "Unknown"),
        "level_index": level
    }