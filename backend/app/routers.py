from fastapi import APIRouter
from models import TestUpdate

router = APIRouter()

@router.get("/")
def all_tests():
    # id и название

@router.get("/{test_id}")
def test_details(test_id: int):
    # id url method header body

@router.post("/start/{test_id}")
def start_test(test_id: int):
    # respon

@router.post("/")
def new_test(test_name: str):
    # создается в бд новый тест и возвращается список всех тестов


@router.patch("/{test_id}/update")
def get_user(test_id: int, test_update: TestUpdate):
    # сохраняется и вохвращается инфа о тесте


@router.get("/start")
def get_user():
    # запускаются тесты и возвращается какие прошли а какие нет

