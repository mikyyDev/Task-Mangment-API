from fastapi import FastAPI

app=FastAPI(
    title="Task managment API",
    description="Backend API for managing tasks, projects, and notes .",
    version="0.1.0",
)

@app.get("/")
async def root():
    return{
        "message": " Task managment API  d"
    }