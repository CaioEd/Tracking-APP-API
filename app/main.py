from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints.routes import routes_router

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'http://127.0.0.1',   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_router)
