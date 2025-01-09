from typing import Optional, Dict

from pydantic import BaseModel


class TestUpdate(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    method: Optional[str] = None
    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict[str, str]] = None


class TestStart(BaseModel):
    id: int
    name: str
    status: int


class TestName(BaseModel):
    id: int
    name_test: str
    method: str = "GET"

    class Config:
        orm_mode = True