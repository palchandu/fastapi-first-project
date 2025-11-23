from fastapi import FastAPI
from app.module.users.route import router
from app.db.database import Base,engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router,prefix="/users",tags=["users"])

@app.get("/")
def root():
    return {"message":"Welcome to the FastAPI application!"}
