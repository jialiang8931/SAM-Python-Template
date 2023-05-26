from . import app

@app.get("/test", tags=['志工統計'], summary='取得當季度第九河川局防汛志工清單', description="QQ123")
def callback(year: str = "2023"):
    year = year.replace(" ", "")
    return f"Hello, { year }"

