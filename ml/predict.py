import joblib
import os
import numpy as np

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../model/rf_fraud_model.pkl"
)

model = joblib.load(MODEL_PATH)

def predict_transaction(features):
    features = np.array(features).reshape(1, -1)  
    prediction = model.predict(features)[0]
    return int(prediction)
