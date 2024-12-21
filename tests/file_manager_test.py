import pytest
from app.services.file_manager import FileManager

@pytest.fixture(scope="function", autouse=True)
def file_manager():
    manager = FileManager(base_dir="tests/test_cases_tests")
    yield manager

    for file in manager.base_dir.glob("*.json"):
        file.unlink()


def test_create_file(file_manager):
    data = {"key": "value"}
    file_manager.create_file("test.json", data)
    file_path = file_manager.base_dir / "test.json"
    assert file_path.exists(), f"Файл {file_path} не был создан."


def test_read_file(file_manager):
    data = {"key": "value"}
    file_manager.create_file("test.json", data)
    result = file_manager.read_file("test.json")
    assert result == data


def test_update_file(file_manager):
    initial_data = {"key": "value"}
    updated_data = {"new_key": "new_value"}
    file_manager.create_file("test.json", initial_data)
    file_manager.update_file("test.json", updated_data)
    file_path = file_manager.base_dir / "test.json"
    assert file_path.exists(), f"Файл {file_path} не существует."
    result = file_manager.read_file("test.json")
    expected_result = {"key": "value", "new_key": "new_value"}
    assert result == expected_result, f"Ожидали: {expected_result}, получили: {result}."


def test_delete_file(file_manager):
    data = {"key": "value"}
    file_manager.create_file("test.json", data)
    file_manager.delete_file("test.json")
    file_path = file_manager.base_dir / "test.json"
    assert not file_path.exists(), f"Файл {file_path} не был удален."


def test_list_files(file_manager):
    file_manager.create_file("test1.json", {"key": "value"})
    file_manager.create_file("test2.json", {"key": "value"})
    files = file_manager.list_files()
    assert "test1.json" in files, "Файл 'test1.json' не найден в списке файлов."
    assert "test2.json" in files, "Файл 'test2.json' не найден в списке файлов."
