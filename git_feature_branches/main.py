from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items")
def get_items():
    return {
        "items": [
            {"id": 1, "name": "item1", "description": "A fancy item", "price": 10.99},
            {"id": 2, "name": "item2", "description": "A useful item", "price": 5.49},
            {"id": 3, "name": "item3", "description": "A rare item", "price": 99.99},
        ]
    }

@app.get("/item")
def get_items():
    return "item1"
