from fastapi import FastAPI

app = FastAPI(
    title = "DefectVision-AI API",
    version ="0.1.0",
    description = "Bu API DefectVision AI uygulamasının FastAPI tabanlı kodlarını içerir."
)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "backend"
    }