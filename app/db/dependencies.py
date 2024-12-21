# запросы через транзакции
"""
from .models import SessionLocal


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        if db:
            db.close()
"""