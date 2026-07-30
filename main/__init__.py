# pyrefly: ignore [missing-import]
from fastapi import FastAPI
# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse

app=FastAPI()

#Stage 1

@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints":["/tasks"]
    }

@app.get("/health")
def health():
    return {
        "status":"ok"
    }


#Stage 2

tasks = [
    {"id":1,"title":"Task 1","done":False},
    {"id":2, "title":"Task 2", "done": False},
    {"id":3, "title":"Task 3", "done": True}
]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            return task
    return JSONResponse(status_code=404, content={"error":f"Task {task_id} Not Found"})