from fastapi import FastAPI
from app.routes import user

app = FastAPI()

app.include_router(user.router, prefix='/api/users', tags=['Users'])

@app.get("/")
def read_root():
    return {"fists": "step"}
