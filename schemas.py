from pydantic import BaseModel, Field
from typing import Optional


# Datos principales de un restaurante
class RestaurantBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    category: str
    city: str
    price: int = Field(..., ge=1, le=3)
    photoUrl: Optional[str] = None


# Datos para crear un restaurante
class RestaurantCreate(RestaurantBase):
    pass


# Datos para actualizar un restaurante
class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    city: Optional[str] = None
    price: Optional[int] = Field(default=None, ge=1, le=3)
    photoUrl: Optional[str] = None


# Datos que devolverá la aplicación
class RestaurantResponse(RestaurantBase):
    id: str
    avgRating: float = 0
    numRatings: int = 0