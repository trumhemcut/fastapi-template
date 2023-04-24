from fastapi import FastAPI

from .routers import companies

app = FastAPI()
app.include_router(companies.router)


@app.get("/")
async def root():
    return {"message": "Hello Tien Nguyen :D"}
