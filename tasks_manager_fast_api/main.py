from fastapi import FastAPI
from api import user_api, task_api

app = FastAPI()

app.include_router(user_api.router, prefix="/users", tags=["users"])
app.include_router(task_api.router, prefix="/task", tags=["tasks"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
