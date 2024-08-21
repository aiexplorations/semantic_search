from pydantic import BaseModel

class Document(BaseModel):
    id: int
    content: str