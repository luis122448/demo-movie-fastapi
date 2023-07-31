from models.movie_model import MovieModel
from schemas.movie_schema import MovieSchema

class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    def findAll(self):
        return self.db.query(MovieModel).all()
    
    def findById(self, movie_id: int):
        return self.db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    
    def findByTitle(self, title: str):
        return self.db.query(MovieModel).filter(MovieModel.title == title).all()
    
    def findByYear(self, year: int):
        return self.db.query(MovieModel).filter(MovieModel.year == year).all()
    
    def findByCategory(self, category: str):
        return self.db.query(MovieModel).filter(MovieModel.category == category).all()
    
    def create(self, movie: MovieSchema):
        tmp = MovieModel(**movie.dict())
        self.db.add(tmp)
        self.db.commit()

    def update(self, movie_id: int, movie: MovieSchema):
        tmp = self.db.query(MovieModel).filter(MovieModel.id == movie_id).first()
        tmp.title = movie.title
        tmp.overview = movie.overview
        tmp.year = movie.year
        tmp.rating = movie.rating
        tmp.category = movie.category
        self.db.commit()

    def delete(self, movie_id: int):
        self.db.query(MovieModel).filter(MovieModel.id == movie_id).delete()
        self.db.commit()