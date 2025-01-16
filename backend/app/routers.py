from typing import Optional

from fastapi import APIRouter, Query, HTTPException
from urllib.parse import unquote
from backend.app.crud import *
import logging

from backend.app.logic.request_sender import send_request, run_all_tests
from backend.app.models import TestStart, TestName, TestUpdate, TestDetails

router = APIRouter()


# все id и name тестов
@router.get("/")
def all_tests():
    tests = get_all_name()
    return [TestName(id=test[0], name_test=test[1], method=test[2]) for test in tests]


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
def new_test(test_name: str, method: str = Query(...)):
    create_test(test_name, method)

    tests = get_all_name()
    return [TestName(id=test[0], name_test=test[1], method=test[2]) for test in tests]


# тест обновляется и возвращается инфа о нем

@router.patch("/update/{test_id}/")
def update_test(
        test_id: int,
        name: Optional[str] = Query(None),
        url: Optional[str] = Query(None),
        method: Optional[str] = Query(None),
        headers: Optional[str] = Query(None),
        body: Optional[str] = Query(None)
):
    headers_decoded = unquote(headers)
    body_decoded = unquote(body)

    try:
        headers_json = json.loads(headers_decoded) if headers_decoded else None
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON format for headers: {str(e)}")

    try:
        body_json = json.loads(body_decoded) if body_decoded else None
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON format for body: {str(e)}")

    # Обновляем тест и получаем результат
    updated_test_dict = update_test_by_id(
        test_id=test_id,
        name_test=name,
        url=url,
        method=method,
        header=headers_json,
        body=body_json,

    )

    return updated_test_dict  # возвращаем только словарь


# start test
@router.post("/tests/start/{test_id}")
def start_test(test_id: int):
    return send_request(test_id)

# start all test
@router.post("/tests/startall")
def start_all_test():
    return run_all_tests()
# delete test
@router.delete("/delete/{test_id}")
def delete_test(test_id: int):
    result = delete_test_by_id(test_id)
    return {"message": f"Test with ID {test_id} was deleted successfully."}


# get a description of all the tests
@router.get("/description")
def descrip_test():
    tests = get_all_description()
    return [TestDetails(id=test[0],
                        name_test=test[1],
                        url=test[2],
                        method=test[3],
                        headers=test[4],
                        body=test[5])
            for test in tests]


"""

@router.get("/tests/start_status")
def start_all_test():
    # запускаются тесты и возвращается какие прошли а какие нет
    
    
# удалить тест

"""
