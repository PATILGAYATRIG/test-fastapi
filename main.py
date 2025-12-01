
from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "This is home page"}

@app.get("/health")
def health():
    return {"status": "healthy","version":1}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)

