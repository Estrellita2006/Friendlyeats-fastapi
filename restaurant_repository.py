from app.core.firebase import db
from app.domain.schemas import RestaurantCreate, RestaurantUpdate


# Colección donde se guardarán los restaurantes
COLLECTION_NAME = "restaurants"


# Crear un restaurante
def create_restaurant(restaurant: RestaurantCreate):
    doc_ref = db.collection(COLLECTION_NAME).document()

    data = restaurant.model_dump()
    data["avgRating"] = 0
    data["numRatings"] = 0

    doc_ref.set(data)

    return {
        "id": doc_ref.id,
        **data
    }


# Obtener todos los restaurantes
def get_restaurants():
    restaurants = []

    docs = db.collection(COLLECTION_NAME).stream()

    for doc in docs:
        restaurant = doc.to_dict()
        restaurant["id"] = doc.id
        restaurants.append(restaurant)

    return restaurants


# Obtener un restaurante por su ID
def get_restaurant(restaurant_id: str):
    doc_ref = db.collection(COLLECTION_NAME).document(restaurant_id)
    doc = doc_ref.get()

    if not doc.exists:
        return None

    restaurant = doc.to_dict()
    restaurant["id"] = doc.id

    return restaurant


# Actualizar un restaurante
def update_restaurant(restaurant_id: str, restaurant: RestaurantUpdate):
    doc_ref = db.collection(COLLECTION_NAME).document(restaurant_id)

    if not doc_ref.get().exists:
        return None

    data = restaurant.model_dump(exclude_unset=True)

    doc_ref.update(data)

    return get_restaurant(restaurant_id)


# Eliminar un restaurante
def delete_restaurant(restaurant_id: str):
    doc_ref = db.collection(COLLECTION_NAME).document(restaurant_id)

    if not doc_ref.get().exists:
        return False

    doc_ref.delete()

    return True


# Filtrar restaurantes por ciudad, categoría y precio
def filter_restaurants(city=None, category=None, price=None):

    # Obtener todos los restaurantes
    docs = db.collection(COLLECTION_NAME).stream()

    restaurants = []

    for doc in docs:
        restaurant = doc.to_dict()
        restaurant["id"] = doc.id

        # Comparar ciudad sin importar mayúsculas o minúsculas
        if city and city.strip().lower() not in restaurant.get("city", "").lower():
            continue

        # Comparar categoría sin importar mayúsculas o minúsculas
        if category and category.strip().lower() not in restaurant.get("category", "").lower():
            continue

        # Comparar precio
        if price is not None and restaurant.get("price") != price:
            continue

        restaurants.append(restaurant)

    return restaurants
