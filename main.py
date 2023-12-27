from fastapi import FastAPI
from routers.events import router, app_router


app = FastAPI()
app.include_router(router)
app.include_router(app_router)
