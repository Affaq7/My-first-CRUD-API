# Task API

A simple CRUD API for managing a to-do list, built with FastAPI. Data is stored in memory (no database) — it resets when the server restarts.

## How to run

1. Clone this repo
2. Create and activate a virtual environment:
```
   python -m venv venv
   venv\Scripts\Activate.ps1
```
3. Install dependencies:
```
   pip install fastapi uvicorn
```
4. Start the server:
```
   uvicorn main:app --reload --port 8000
```
5. Visit `http://localhost:8000/docs` for interactive Swagger UI

## Endpoints

| Method | Path          | Description              |
|--------|---------------|---------------------------|
| GET    | /             | API info                  |
| GET    | /health       | Health check               |
| GET    | /tasks        | List all tasks             |
| GET    | /tasks/{id}   | Get one task by id         |
| POST   | /tasks        | Create a new task          |
| PUT    | /tasks/{id}   | Update a task              |
| DELETE | /tasks/{id}   | Delete a task               |

## Example request & Output Screenshots (Curl)

### Stage 3 (POST)
![alt text](/Screenshots/Stage3.png)

### Stage 4 (PUT & DELETE)
![alt text](/Screenshots/Stage4.png)

### Stage 5 (Swagger UI)
See the [assignment brief](CRUD%20API%20-%20Swagger%20UI.pdf).