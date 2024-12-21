"""

import pytest
from app import open_create_test_window, get_current_window, open_create_test_window, save_test, get_all_tests, create_test, delete_test, get_all_tests

# Тест-кейс № 1: Создание нового теста
@pytest.fixture(scope="function")
def test_open_create_test_window():
    response = open_create_test_window()

    # Ожидаемый результат: Открывается окно создания нового теста
    assert response == "Create test window opened"

    # Проверка, что все поля пусты и доступны для редактирования
    current_window = get_current_window()
    assert current_window["name"] == ""
    assert current_window["description"] == ""
    assert current_window["editable"] is True

# Тест-кейс № 2: Добавление данных в тест
@pytest.fixture(scope="function")
def test_create_and_save_new_test():
    # Шаг 1: Открыть окно создания теста
    open_create_test_window()

    # Шаг 2: Ввести данные
    new_test = {"name": "Тест 1", "description": "Описание теста 1", "file_path" : "Путь к JSON-файлу"}
    response = save_test(new_test)

    # Ожидаемый результат: Тест успешно сохранен
    assert response == "Test saved successfully"

    # Шаг 3: Проверка списка тестов
    tests = get_all_tests()
    assert len(tests) == 1
    assert tests[0]["name"] == "Тест 1"
    assert tests[0]["description"] == "Описание теста 1"

# Тест-кейс № 3: Удаление существующего теста
@pytest.fixture(scope="function")
def test_delete_existing_test():
    # Шаг 1: Получить ID теста
    test = get_all_tests()[0]
    test_id = test["id"]

    # Шаг 2: Удалить тест
    response = delete_test(test_id)
    assert response == "Test deleted successfully"

    # Шаг 3: Проверка, что тест удален
    tests_after = get_all_tests()
    assert len(tests_after) == 0

# Тест-кейс № 4: Редактирование существующего теста
@pytest.fixture(scope="function")
def test_edit_existing_test():
    # Шаг 1: Получить ID теста
    test = get_all_tests()[0]
    test_id = test["id"]

    # Шаг 2: Редактировать описание теста
    updated_data = {"description": "Обновленное описание"}
    response = edit_test(test_id, updated_data)
    assert response == "Test edited successfully"

    # Шаг 3: Проверка обновленного описания
    updated_test = get_all_tests()[0]
    assert updated_test["description"] == "Обновленное описание"

"""