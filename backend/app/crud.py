import json

from backend.app.db import db_models


# Выбрать все тесты
def get_all_tests():
    with db_models.session() as session:
        tests = session.query(db_models.Test).all()
        return tests

# Выбрать все id и name
def get_all_name():
    with db_models.session() as session:
        tests = session.query(db_models.Test.id, db_models.Test.name).all()
        return tests


# Тест по ID
def get_test_by_id(test_id):

    with db_models.session() as session:
        print("!!!!")
        test = session.query(db_models.Test).filter(db_models.Test.id == test_id).first()
        return test



# Создать тест по названию
def create_test(name_test):
    with db_models.session() as session:
        new_test = db_models.Test(name=name_test)
        session.add(new_test)
        session.commit()
        return new_test


# Изменить тест по ID
def update_test_by_id(test_id, name_test=None, url=None, method=None, header=None, body=None):
    with db_models.session() as session:
        test = session.query(db_models.Test).filter(db_models.Test.id == test_id).first()

        if isinstance(header, str):
            header = json.loads(header)
        if isinstance(body, str):
            body = json.loads(body)

        if test:
            if name_test:
                test.name = name_test
            if url:
                test.url = url
            if method:
                test.method = method
            if header:
                test.header = header
            if body:
                test.body = body
            session.commit()
            return test
        return None

