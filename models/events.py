from typing import Optional, List

from beanie import Document
from pydantic import BaseModel


class Event(Document):
    creator: Optional[str]
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
    
    class Settings:
        collection = "events"


    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI",
                "image": "https://linktomyimage.com/image.png",
                "description": "sample of description",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

   

class EventUpdate(BaseModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI",
                "image": "https://image_route",
                "description": "Somesort of description",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }