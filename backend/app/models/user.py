from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.db.base import Base


class CoreClass(Base):
    __abstract__ = True

    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(CoreClass):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    logins = relationship("Login", back_populates="users")


class Login(CoreClass):
    __tablename__ = 'login_history'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    email = Column(String(50), unique=True, nullable=False)
    login_date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship("User", back_populates="logins")







