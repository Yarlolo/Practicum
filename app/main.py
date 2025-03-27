from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.session import engine, Base_class
from datetime import datetime, timezone
from app.api.endpoints import auth, graph

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Старт...')
    Base_class.metadata.create_all(bind=engine)
    yield
    print('Завершение...')

app = FastAPI(lifespan=lifespan)

app.include_router(auth.router, prefix='/api', tags=['auth'])
app.include_router(graph.router, prefix='/api', tags=['graph'])

@app.get("/")
def read_root():
    return {
        'сообщение': 'Добро пожаловать в API для работы с графами',
        'доступные_методы': {
            'регистрация': '/api/регистрация/',
            'авторизация': '/api/вход/',
            'поиск_пути': '/api/кратчайший-путь/'
        },
        'время_сервера': datetime.now(timezone.utc).isoformat()
    }
