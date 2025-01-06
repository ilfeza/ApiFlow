from fastapi import APIRouter
from models import *
from crud import *


router = APIRouter()

# все id и name тестов
@router.get("/bu", response_model=list[TestName])
def all_tests():
    tests = get_all_name()
    return [TestName(id=test[0], name_test=test[1]) for test in tests]

"""

@router.get("/{test_id}")
def test_details(test_id: int):
    # id url method header body

@router.post("/tests/start/{test_id}")
def start_test(test_id: int):
    # respon

@router.post("/")
def new_test(test_name: str):
    # создается в бд новый тест и возвращается список всех тестов


@router.patch("/{test_id}/update")
def get_user(test_id: int, test_update: TestUpdate):
    # сохраняется и вохвращается инфа о тесте


@router.get("/tests/start_status")
def get_user():
    # запускаются тесты и возвращается какие прошли а какие нет

"""