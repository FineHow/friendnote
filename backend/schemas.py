from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    openid: str
    nickname: str
    avatar_url: Optional[str]

class DiaryCreate(BaseModel):
    user_id: int
    content: str
    visibility: str

class CircleCreate(BaseModel):
    name: str
    creator_id: int