from fastapi import FastAPI

from .routers import companies
from .routers import users
from .routers import tasks

app = FastAPI()
app.include_router(companies.router)
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Hello Tien Nguyen :D"}
