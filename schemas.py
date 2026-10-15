from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class NoteCreate(BaseModel):
    title: str
    content: str | None = None

class NoteOut(BaseModel):
    id: int
    title: str
    content: str | None

    class Config:
        from_attributes = True