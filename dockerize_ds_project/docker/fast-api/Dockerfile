FROM tiangolo/uvicorn-gunicorn:python3.8
WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]