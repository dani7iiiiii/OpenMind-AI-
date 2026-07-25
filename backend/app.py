from fastapi import FastAPI

app = FastAPI(title="OpenMind AI")

@app.get("/")
def root():
    return {"message": "Welcome to OpenMind AI"}
