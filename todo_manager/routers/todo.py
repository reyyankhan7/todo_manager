from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from todo_manager import crud, schemas
from todo_manager.database import get_db

router = APIRouter(prefix="/todos", tags=["To-Do"])

@router.get("/", response_model=List[schemas.TodoResponse])
def read_todos(status: Optional[str] = Query(None), db: Session = Depends(get_db)):
    return crud.get_todos(db, status)

@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="To-Do not found")
    return db_todo

@router.post("/", response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)

@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    updated_todo = crud.update_todo(db, todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="To-Do not found")
    return updated_todo

@router.delete("/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    deleted_todo = crud.delete_todo(db, todo_id)
    if not deleted_todo:
        raise HTTPException(status_code=404, detail="To-Do not found")
    return {"message": "To-Do deleted"}
