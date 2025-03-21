from fastapi import FastAPI
from routers import diary

app = FastAPI()

# 注册路由
app.include_router(diary.router, prefix="/api", tags=["Diary"])

# 启动提示
@app.get("/")
def read_root():
    return {"message": "Welcome to Friends' Diary API!"}