# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Response
# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse
# pyrefly: ignore [missing-import]
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

#Stage 1

@app.get("/")
def root():
    """Returns API name and version."""
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints":["/tasks"]
    }

@app.get("/health")
def health():
    """Checks if the server is alive."""
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
    """Returns a list of all tasks in the in-memory database."""
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id:int):
    """Returns a single task matching the provided ID."""
    for task in tasks:
        if task["id"]==task_id:
            return task
    return JSONResponse(status_code=404, content={"error":f"Task {task_id} Not Found"})

#stage 3
class TaskCreate(BaseModel):
    title: Optional[str]=None

@app.post("/tasks", status_code=201, responses={100:{"description":"Invalid Input - Title missing or empty" }})
def create_task(task:TaskCreate):
    """Creates a new task and assigns it a unique ID."""
    if not task.title or not task.title.strip():
        return JSONResponse(status_code=400, content={"error":"Title is required"})

    new_id=max((t["id"] for t in tasks), default=0)+1
    new_task = {"id":new_id, "title": task.title, "done":False}
    tasks.append(new_task)
    return new_task

#stage 4
class TaskUpdate(BaseModel):
    title: str | None= None
    done: bool | None = None

@app.put("/tasks/{id}", responses={400:{"description":"Invalid Body"}, 404:{"description":"Task not found"}})
def update_task(id:int, task_in:TaskUpdate):
    """Updates the title or completion status of an existing task."""
    if task_in.title is None and task_in.done is None:
        return JSONResponse(status_code=400, content={"error": "Body cannot be empty"})
    
    if task_in.title is not None and not task_in.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title cannot be empty"})
    
    for task in tasks:
        if task["id"]==id:
            if task_in.title is not None:
                task["title"]=task_in.title.strip()
            if task_in.done is not None:
                task["done"]=task_in.done
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})

@app.delete("/tasks/{id}", responses={404: {"description": "Task not found"}})
def delete_task(id:int):
    """Deletes a task from the list based on its ID."""
    for i, task in enumerate(tasks):
        if task["id"]==id:
            tasks.pop(i)
            return Response(status_code=204)
    return JSONResponse(status_code=404, content={"error":f"Task {id} not found"})

