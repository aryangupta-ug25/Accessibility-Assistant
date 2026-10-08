from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

@app.get("/api/health")
def health_check():
    return {"status": "success", "message": "Frontend-to-backend infrastructure is live!"}
