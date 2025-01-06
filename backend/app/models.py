from typing import Optional, Dict

from pydantic import BaseModel


class TestUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    method: Optional[int] = None
    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict[str, str]] = None


class TestStart(BaseModel):
    id: int
    name: str
    status: int


"""
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from backend.app.db.database import Base
from sqlalchemy.ext.declarative import declarative_base
import json
from datetime import datetime

Base = declarative_base()


class Test(Base):
    __tablename__ = 'tests'

    TestId = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Description = Column(Text)
    Created_at = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String)

    # добавить просмотр всех результатов для теста
    # results = relationship("TestResult", back_populates="test", cascade="all, delete-orphan")


class TestResult(Base):
    __tablename__ = 'test_results'

    ResultID = Column(Integer, primary_key=True, autoincrement=True)
    Test_id = Column(Integer, ForeignKey('tests.TestId'), nullable=False)
    executed_at = Column(DateTime, default=datetime.utcnow)
    Status = Column(String, nullable=False)
    Execution_log = Column(Text)

    test = relationship("Test", back_populates="results")



engine = create_engine('sqlite:///apiflow.db')  # Можно заменить на любой другой тип базы данных

Base.metadata.create_all(engine)  # Создание всех таблиц в базе данных

# Создание сессии для работы с БД
Session = sessionmaker(bind=engine)
session = Session()

"""
