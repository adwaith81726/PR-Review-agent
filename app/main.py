from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="PR Review Agent")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "PR Review Agent API is running 🚀"}
