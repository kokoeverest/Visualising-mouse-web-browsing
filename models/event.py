from pydantic import BaseModel


class Event(BaseModel):
    id: str | None = None
    c_x: str | int 
    c_y: str | int
    time: str
    image_data: bytes | None = None