from fastapi import FastAPI, Request, APIRouter
from routers.router import user_router, restaraunt_router
from routers.urls import template_router
from database.DB import engine
from models.model import Model


app = FastAPI(title="Платформа по доставке еды")


app.include_router(user_router)
app.include_router(restaraunt_router)
app.include_router(template_router)


if __name__=="__main__":
    import uvicorn
    Model.metadata.create_all(engine)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)