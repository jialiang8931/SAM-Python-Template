from . import app

@app.get("/test/info", tags=['測試'], summary='測試111', description="description")
def callback(year: str = "2023"):
    return f"Hello, { year }"