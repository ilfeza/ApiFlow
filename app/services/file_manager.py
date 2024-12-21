from pathlib import Path
import json
from logger_config import logger

logger.info("Logging initialized")

class FileManager:
    def __init__(self, base_dir: str = "test_cases"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)

    def create_file(self, file_name: str, data: dict) -> str:
        if not file_name.endswith(".json"):
            file_name += ".json"
        file_path = self.base_dir / file_name

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        logger.info(f"File created at path: {file_path}")
        return str(file_path)

    def read_file(self, file_name: str) -> dict:
        file_path = self.base_dir / file_name

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        logger.info(f"File read: {file_name}")
        return data

    def update_file(self, file_name: str, new_data: dict) -> str:
        file_path = self.base_dir / file_name

        data = self.read_file(file_name)
        data.update(new_data)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        logger.info(f"File updated: {file_name}")
        return str(file_path)

    def delete_file(self, file_name: str) -> None:
        file_path = self.base_dir / file_name
        file_path.unlink()

        logger.info(f"File deleted: {file_name}")

    def list_files(self) -> list:
        files = [f.name for f in self.base_dir.glob("*.json")]
        logger.info(f"Files listed: {files}")
        return files

