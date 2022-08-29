from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return "Main page"


if __name__ == "__main__":
    # right address is http://127.0.0.1:8001/
    uvicorn.run(app, host="0.0.0.0", port=8001)
