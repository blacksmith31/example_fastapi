from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

# Pydantic models
# USERS
class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    # tells pydandic how to handle sqlalchemy response objects
    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# POSTS
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # tells pydandic how to handle sqlalchemy response objects
    class Config:
        orm_mode=True
    
class PostOut(PostBase):
    Post: Post
    votes: int

    class Config:
        orm_mode=True

# TOKENS
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
# VOTE
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
