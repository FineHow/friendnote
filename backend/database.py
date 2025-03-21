from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 替换为您的 MySQL 配置
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/diary_app"

# 初始化 SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 提供数据库连接的依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()