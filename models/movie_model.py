from config.database import base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class MovieModel(base):

    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    overview = Column(String(500), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    category = Column(String(50), nullable=False)