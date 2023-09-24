from typing import Any, Dict, Optional
import mlflow

class PromoterGPT(mlflow.pyfunc.PythonModel):
    def __init__(self, predictor):
        self.predictor = predictor

    def predict(self, context, model_input):
        output = self.predictor.generate(model_input, 50, temperature=0.8, top_k=4)
        return decode(y[0].tolist())