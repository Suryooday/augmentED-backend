from pydantic import BaseModel
from typing import Optional
from enum import Enum


class UserBase(BaseModel):
    email: str
    username: str


class UserIn(UserBase):
    password: str


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    hashed_password: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class Book(BaseModel):
    # TODO Check for errors and clean up this dog💩
    id: int
    subject: str
    document: Optional[bytes] = None
