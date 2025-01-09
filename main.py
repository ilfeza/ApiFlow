from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import router
print(router)


app = FastAPI(title="Приложение для тестирования API")

app.include_router(router, tags=["Tests"])

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить доступ с любых источников. Для безопасности укажите конкретный домен, например, ["http://localhost:63342"]
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP-методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"],  # Разрешить все заголовки
)

# Пример данных
tasks = [
    {"id": 1, "title": "Разработка API", "status": "В процессе", "deadline": "2024-12-30", "description": "Создать REST API для управления задачами"},
    {"id": 2, "title": "Тестирование", "status": "Завершено", "deadline": "2024-12-28", "description": "Провести тестирование системы"},
    {"id": 3, "title": "Написание документации", "status": "Не начато", "deadline": "2024-12-31", "description": "Написать документацию для разработчиков"},
]

@app.get("/tasks")
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")
