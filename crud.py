from sqlalchemy.orm import Session
import models, schemas
# Create a new to-do
def create_todo(db: Session, todo: schemas.ToDoCreate):
    db_todo = models.ToDo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Get all to-dos
def get_todos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ToDo).offset(skip).limit(limit).all()

# Get a specific to-do by ID
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()

# Update a to-do
def update_todo(db: Session, todo_id: int, todo: schemas.ToDoUpdate):
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo is None:
        return None
    db_todo.title = todo.title
    db_todo.description = todo.description
    db_todo.completed = todo.completed
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Delete a to-do
def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return db_todo
    return None
