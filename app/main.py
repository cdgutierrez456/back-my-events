from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.user import router as user_router
from app.routes.event import router as event_router
from app.routes.profile import router as profile_router
# from .database import create_tables
import app.models

app = FastAPI()

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_router, prefix='/api/users', tags=['Users'])
app.include_router(event_router, prefix='/api/events', tags=['Events'])
app.include_router(profile_router, prefix='/api/profiles', tags=['Profiles'])

# @app.on_event("startup")
# async def on_startup():
#     await create_tables()

@app.get("/")
def read_root():
    return {"API": "MyEvents - Welcome"}
