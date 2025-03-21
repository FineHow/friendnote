from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from .database import Base

# 用户表
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    openid = Column(String(50), unique=True, index=True)
    nickname = Column(String(50))
    avatar_url = Column(String(200))

# 日记表
class Diary(Base):
    __tablename__ = "diaries"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    date = Column(Date)
    visibility = Column(String(50))
    user = relationship("User")

# 朋友圈表
class Circle(Base):
    __tablename__ = "circles"
    id = Column(Integer, primary_key=True, index=True)
    creator_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(50))
    creator = relationship("User")

# 圈成员表
class CircleMember(Base):
    __tablename__ = "circle_members"
    id = Column(Integer, primary_key=True, index=True)
    circle_id = Column(Integer, ForeignKey("circles.id"))
    user_id = Column(Integer, ForeignKey("users.id"))