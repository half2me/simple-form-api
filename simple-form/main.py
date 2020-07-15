from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def rows():
    return {"message": "Hello World"}


@app.post("/")
async def add():
    return {"message": "Hello World"}
