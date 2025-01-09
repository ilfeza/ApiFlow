from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import router
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
