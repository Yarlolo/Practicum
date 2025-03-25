from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base_class

class User(Base_class):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)