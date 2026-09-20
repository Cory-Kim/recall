from fastapi import FastAPI

app = FastAPI(
    title="RECALL API",
    description="Local-first search for your files",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

