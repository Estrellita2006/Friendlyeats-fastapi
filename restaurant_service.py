from app.repositories import restaurant_repository
from app.domain.schemas import RestaurantCreate, RestaurantUpdate


# Registrar un restaurante
def create_restaurant(restaurant: RestaurantCreate):
    return restaurant_repository.create_restaurant(restaurant)


# Mostrar todos los restaurantes
def get_restaurants():
    return restaurant_repository.get_restaurants()


# Buscar un restaurante
def get_restaurant(restaurant_id: str):
    return restaurant_repository.get_restaurant(restaurant_id)


# Modificar un restaurante
def update_restaurant(restaurant_id: str, restaurant: RestaurantUpdate):
    return restaurant_repository.update_restaurant(
        restaurant_id,
        restaurant
    )


# Eliminar un restaurante
def delete_restaurant(restaurant_id: str):
    return restaurant_repository.delete_restaurant(restaurant_id)

# Filtrar restaurantes
def filter_restaurants(city=None, category=None, price=None):
    return restaurant_repository.filter_restaurants(
        city=city,
        category=category,
        price=price
    )
