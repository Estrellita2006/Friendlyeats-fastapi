
from fastapi import APIRouter, HTTPException

from app.domain.schemas import (
    RestaurantCreate,
    RestaurantUpdate
)

from app.services import restaurant_service


router = APIRouter(
    prefix="/restaurants",
    tags=["Restaurantes"]
)


# Filtrar restaurantes por ciudad, categoría o precio
@router.get("/search/filter")
def filter_restaurants(
    city: str = None,
    category: str = None,
    price: int = None
):
    return restaurant_service.filter_restaurants(
        city=city,
        category=category,
        price=price
    )

# Registrar un restaurante
@router.post("/")
def create_restaurant(restaurant: RestaurantCreate):
    return restaurant_service.create_restaurant(restaurant)


# Mostrar todos los restaurantes
@router.get("/")
def get_restaurants():
    return restaurant_service.get_restaurants()


# Buscar un restaurante por ID
@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: str):
    restaurant = restaurant_service.get_restaurant(restaurant_id)

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return restaurant


# Actualizar un restaurante
@router.put("/{restaurant_id}")
def update_restaurant(
    restaurant_id: str,
    restaurant: RestaurantUpdate
):
    updated = restaurant_service.update_restaurant(
        restaurant_id,
        restaurant
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return updated


# Eliminar un restaurante
@router.delete("/{restaurant_id}")
def delete_restaurant(restaurant_id: str):
    deleted = restaurant_service.delete_restaurant(restaurant_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Restaurante no encontrado"
        )

    return {"mensaje": "Restaurante eliminado correctamente"}
