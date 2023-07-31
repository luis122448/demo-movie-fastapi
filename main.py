from fastapi import FastAPI, HTTPException, Body, Path, Query, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from config.database import session, engine, base
from middlewares.error_handler import ErrorHandler
from routers.movie_router import movie_router
from routers.auth import auth_router

app = FastAPI()
app.title = "My First API"
app.version = "0.0.1"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(auth_router)

base.metadata.create_all(bind=engine)

@app.get("/", tags=["Home"])
def message():
    return HTMLResponse(content="<h1>Hello World!</h1>", status_code=200)