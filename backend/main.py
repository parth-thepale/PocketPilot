from fastapi import FastAPI

app = FastAPI(
    title="PocketPilot API",
    description="Organize. Search. Remember.",
    version="0.1.0"
)

@app.get("/")
def home():
    return {
        "message": "PocketPilot API is Running 🚀",
        "status": "success"
    }