from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import companies
from .routers import users
from .routers import tasks

app = FastAPI()
app.include_router(companies.router)
app.include_router(users.router)
app.include_router(tasks.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello Tien Nguyen :D"}
