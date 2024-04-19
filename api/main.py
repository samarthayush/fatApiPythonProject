# uvicorn --app-dir=. api.main:app --reload
# .venv\Scripts\activate
# python -m pytest /tests/
# pip install -r requirements-dev.txt

from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def hello():
    return {"message": "hello"}