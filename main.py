from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud,schemas,database

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def get_data():
    return {"message": "Welcome to the FastAPI To-Do API"}

@app.post("/todos/", response_model=schemas.ToDo)
def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.get("/todos/", response_model=list[schemas.ToDo])
def read_todos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_todos(db=db, skip=skip, limit=limit)

@app.get("/todos/{todo_id}", response_model=schemas.ToDo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="To-do not found")
    return db_todo

@app.put("/todos/{todo_id}", response_model=schemas.ToDo)
def update_todo(todo_id: int, todo: schemas.ToDoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db=db, todo_id=todo_id, todo=todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="To-do not found")
    return db_todo

@app.delete("/todos/{todo_id}", response_model=schemas.ToDo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="To-do not found")
    return db_todo
