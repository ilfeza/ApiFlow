import json

from backend.app.db import db_models


# Для таблицы TESTS

# Выбрать все тесты
def get_all_tests():
    with db_models.session() as session:
        tests = session.query(db_models.Test).all()
        return tests


# Выбрать все id и name
def get_all_name():
    with db_models.session() as session:
        tests = session.query(db_models.Test.id, db_models.Test.name, db_models.Test.method).all()
        return tests

# Выбрать все тесты
def get_all_description():
    with db_models.session() as session:
        tests = session.query(db_models.Test.id,
                              db_models.Test.name,
                              db_models.Test.url,
                              db_models.Test.method,
                              db_models.Test.header,
                              db_models.Test.body).all()
        return tests

# Тест по ID
def get_test_by_id(test_id):
    with db_models.session() as session:
        test = session.query(db_models.Test).filter(db_models.Test.id == test_id).first()
        return test


# Создать тест по названию
def create_test(name_test, test_method):
    with db_models.session() as session:
        new_test = db_models.Test(name=name_test, method=test_method)
        session.add(new_test)
        session.commit()
        return new_test


# Изменить тест по ID


def update_test_by_id(test_id: int, name_test: str, url: str, method: str, header: dict, body: dict):
    with db_models.session() as session:

        test = session.query(db_models.Test).filter(db_models.Test.id == test_id).first()
        if not test:
            return None

        if name_test:
            test.name = name_test
        if url:
            test.url = url
        if method:
            test.method = method
        if header or header == {}:
            test.header = header
        if body or body == {}:
            test.body = body

        session.commit()  # Сохраняем изменения
        session.refresh(test)  # Обновляем объект с актуальными данными из базы
        return {
            "id": test.id,
            "name": test.name,
            "url": test.url,
            "method": test.method,
            "headers": test.header,
            "body": test.body
        }


# Удаление теста
def delete_test_by_id(test_id: int):
    with db_models.session() as session:
        test = session.query(db_models.Test).filter(db_models.Test.id == test_id).first()
        if not test:
            return False
        session.delete(test)
        session.commit()
        return True


# Для таблицы TEST_RESULT

# добавить резултат теста
def create_result(id_test, status, execution_log):
    with db_models.session() as session:
        new_result = db_models.TestResult(
            id_test=id_test,
            status=status,
            execution_log=execution_log
        )

        session.add(new_result)
        session.commit()
        return new_result
