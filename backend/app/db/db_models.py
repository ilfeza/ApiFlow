from sqlalchemy import create_engine, Column, Integer, String, Text, JSON, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Test(Base):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    url = Column(Text, nullable=True)
    method = Column(Text, nullable=True)
    header = Column(JSON, nullable=True)
    body = Column(JSON, nullable=True)

class TestResult(Base):
    __tablename__ = 'test_results'
    id_result = Column(Integer, primary_key=True, autoincrement=True)
    id_test = Column(Integer, ForeignKey('tests.id', ondelete="CASCADE"), nullable=False)
    status = Column(String, nullable=False)
    execution_log = Column(JSON, nullable=True)

DATABASE_URL = "sqlite:///backend/app/apiFlow.db"

engine = create_engine(DATABASE_URL, echo=True)

session = sessionmaker(engine)

