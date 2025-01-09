from fastapi import APIRouter, HTTPException
from models import *
from crud import *
import logging

router = APIRouter()

import json
from logic.request_sender import send_request

response = send_request(3)

# Выводим весь объект response в формате JSON
print(json.dumps(response.json(), indent=4))


# все id и name тестов
@router.get("/")
def all_tests():
    tests = get_all_name()
    return [TestName(id=test[0], name_test=test[1]) for test in tests]


# описание теста
@router.get("/details/{test_id}", response_model=TestUpdate)
def test_details(test_id: int):
    description = get_test_by_id(test_id)
    logging.info(f"Fetched description: {description}")

    return TestUpdate(
        name=description.name,
        url=description.url,
        method=description.method,
        headers=description.header,
        body=description.body,
    )
# новый тест
@router.post("/new_test/{test_name}")
def new_test(test_name: str):
    create_test(test_name)

    tests = get_all_name()
    return [TestName(id=test[0], name_test=test[1]) for test in tests]

# тест обновляется и возвращается инфа о нем
@router.patch("/{test_id}/update")
def update_test(test_id: int, test_update: TestUpdate):
    updated_test = update_test_by_id(
        test_id=test_id,
        name_test=test_update.name,
        url=test_update.url,
        method=test_update.method,
        header=test_update.headers,
        body=test_update.body,
    )

    return {
        "id": updated_test.id,
        "name": updated_test.name,
        "url": updated_test.url,
        "method": updated_test.method,
        "headers": updated_test.header,
        "body": updated_test.body,
    }





"""



@router.get("/tests/start_status")
def get_user():
    # запускаются тесты и возвращается какие прошли а какие нет
    
    
# удалить тест

"""
