from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def show_root():
    return {"message": "Hello from fastapi-demo!"}


@app.get("/products/")

def show_products():
    return "This is from product page!"


def main():
    print("Hello from fastapi-demo!")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)