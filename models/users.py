from beanie import Document

from pydantic import BaseModel, EmailStr


class User(Document):
    email: EmailStr
    password: str

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user_email@email.corn",
                "password": "any_password"
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str