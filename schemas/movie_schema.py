from typing import Optional, List
from pydantic import BaseModel, Field

class MovieSchema(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=50)
    overview: str = Field(..., min_length=1, max_length=500)
    year: int = Field(..., gt=1900, lt=2100)
    rating: float = Field(..., gt=0, lt=10)
    category: str = Field(..., min_length=1, max_length=50)

    model_config = {
     "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción"
                }
            ]
        }
    }
