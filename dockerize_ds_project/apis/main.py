from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/predict_salary/")
async def predict_salary(employee_age: int = 23):
    """  Uses a saved model to predict argument 
        passed as employee_age
    """
    filename = '/code/app/models/simple_linear_regression_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    return JSONResponse(loaded_model.predict([[employee_age]])[0])