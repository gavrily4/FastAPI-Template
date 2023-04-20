from datetime import datetime

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    created_on: datetime | None
    updated_on: datetime | None


class UserCreateSchema(BaseModel):
    name: str


class UserUpdateSchema(UserCreateSchema):
    id: int
