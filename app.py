from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_text():
    return {"text": "hello world"}
