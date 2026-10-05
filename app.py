from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
def read_products():
    return []
