from fastapi import FastAPI

app = FastAPI(title="FastAPI Project")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello FastAPI"}
