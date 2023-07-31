from fastapi import FastAPI, HTTPException, Body, Path, Query, Request, Depends, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import session, engine, base
from models.movie_model import MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBarer
from services.movie_service import MovieService
from schemas.movie_schema import MovieSchema
from typing import Optional, List

movie_router = APIRouter()

@movie_router.get("/movies", tags=["movie"], response_model=List[MovieSchema], dependencies=[Depends(JWTBarer())])
def get_movies():
    db = session()
    result = jsonable_encoder(MovieService(db).findAll())
    return JSONResponse(content=result, status_code=200)

@movie_router.get("/movies/{movie_id}", tags=["movie"], response_model=MovieSchema)
def get_movie(movie_id: int = Path(... , ge=1, le=2000)):
    db = session()
    result = jsonable_encoder(MovieService(db).findById(movie_id))
    if not result:
        raise HTTPException(status_code=404, detail={"message": "Movie not found"})
    return JSONResponse(content=result, status_code=200)

@movie_router.get("/movies/by-title/", tags=["movie"], response_model=List[MovieSchema])
def get_movie_by_title(title: str = Query(None, min_length=1, max_length=50)):
    db = session()
    result = jsonable_encoder(db.query(MovieModel).filter(MovieModel.title == title).all())
    if not result:
        raise HTTPException(status_code=404, detail={"message": "Movie not found"})
    return JSONResponse(content=result, status_code=200)

@movie_router.get("/movies/by-year/", tags=["movie"], response_model=List[MovieSchema])
def get_movie_by_year(year: int):
    db = session()
    result = jsonable_encoder(db.query(MovieModel).filter(MovieModel.year == year).all())
    if not result:
        raise HTTPException(status_code=404, detail={"message": "Movie not found"})
    return JSONResponse(content=result, status_code=200)

@movie_router.get('/movies/by-category', tags=['movies'], response_model=List[MovieSchema], status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)) -> List[MovieSchema]:
    db = session()
    result = jsonable_encoder(db.query(MovieModel).filter(MovieModel.category == category).all())
    if not result:
        raise HTTPException(status_code=404, detail={"message": "Movie not found"})
    return JSONResponse(content=result, status_code=200)

@movie_router.post('/movies', tags=["movie"], response_model=dict)
def create_movie(movie: MovieSchema):
    db = session()
    MovieService(db).create(movie)
    return JSONResponse(content={"message":"success"}, status_code=201)

@movie_router.put('/movies/{movie_id}', tags=["movie"], response_model=dict)
def update_movie(movie_id: int, movie: MovieSchema):
    db = session()
    result = MovieService(db).findById(movie_id)
    if not result:
        raise HTTPException(status_code=404, detail={"message": "Movie not found"})
    MovieService(db).update(movie_id, movie)
    return JSONResponse(content={"message":"success"}, status_code=201)

@movie_router.delete('/movies/{movie_id}', tags=["movie"], response_model=dict)
def delete_movie(movie_id: int):
    db = session()
    result = MovieService(db).findById(movie_id)
    if not result:
        raise HTTPException(status_code=404, detail={"message": "Movie not found"})
    MovieService(db).delete(movie_id)
    return JSONResponse(content={"message":"success"}, status_code=201)
