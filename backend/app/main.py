from fastapi import FastAPI

app = FastAPI(
    title="Sage AI Interview Agent",
    description="AI-powered adaptive interview platform",
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "application": "Sage AI Interview Agent",
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }