# init_db.py
from database import engine
from models import Base

# 创建所有表
Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")