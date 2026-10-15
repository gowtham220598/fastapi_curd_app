from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import models
import schemas
import auth
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRUD APPLICATIONS")
app.description = " Gowtham M "

#register
@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = models.User(
        username=user.username,
        hashed_password=auth.hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}


#login
@app.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form.username).first()
    if not user or not auth.verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Wrong username or password")

    return {
        "username": user.username,
        "access_token": auth.create_token(user.username),
        "token_type": "bearer",
    }


# create
@app.post("/notes", response_model=schemas.NoteOut)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    new_note = models.Note(title=note.title, content=note.content, owner_id=current_user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


# read(all)
@app.get("/notes", response_model=list[schemas.NoteOut])
def list_notes(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    return db.query(models.Note).filter(models.Note.owner_id == current_user.id).all()


# read(one)
@app.get("/notes/{note_id}", response_model=schemas.NoteOut)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    note = db.query(models.Note).filter(
        models.Note.id == note_id, models.Note.owner_id == current_user.id
    ).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


# update
@app.put("/notes/{note_id}", response_model=schemas.NoteOut)
def update_note(
    note_id: int,
    data: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    note = db.query(models.Note).filter(
        models.Note.id == note_id, models.Note.owner_id == current_user.id
    ).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note.title = data.title
    note.content = data.content
    db.commit()
    db.refresh(note)
    return note


# delete
@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user),
):
    note = db.query(models.Note).filter(
        models.Note.id == note_id, models.Note.owner_id == current_user.id
    ).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}