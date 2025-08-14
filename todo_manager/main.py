from fastapi import FastAPI
from todo_manager.database import Base, engine
from todo_manager.routers.todo import router as todo_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List Manager API")
app.include_router(todo_router)
