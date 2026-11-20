
from fastapi import APIRouter, Request, Form, HTTPException
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from app.services import restaurant_service
from app.domain.schemas import RestaurantCreate, RestaurantUpdate


router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# Página de inicio
@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )



# Mostrar todos los restaurantes y aplicar filtros
@router.get("/restaurants")
async def show_restaurants(
    request: Request,
    city: str = None,
    category: str = None,
    price: int = 0
):
    # Si no se selecciona precio, mostrar todos
    if price == 0:
        price = None

    restaurants = restaurant_service.filter_restaurants(
        city=city,
        category=category,
        price=price
    )

    return templates.TemplateResponse(
        request=request,
        name="restaurants.html",
        context={
            "restaurants": restaurants,
            "city": city,
            "category": category,
            "price": price
        }
    )



# Ver detalles de un restaurante
@router.get("/restaurants/{restaurant_id}/detail")
async def restaurant_detail(request: Request, restaurant_id: str):
    restaurant = restaurant_service.get_restaurant(restaurant_id)

    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    return templates.TemplateResponse(
        request=request,
        name="restaurant_detail.html",
        context={"restaurant": restaurant}
    )


# Mostrar formulario para registrar
@router.get("/restaurants/new")
async def new_restaurant(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="restaurant_form.html",
        context={
            "title": "Registrar restaurante",
            "action": "/restaurants/new",
            "restaurant": None
        }
    )


# Guardar nuevo restaurante
@router.post("/restaurants/new")
async def create_restaurant(
    name: str = Form(...),
    category: str = Form(...),
    city: str = Form(...),
    price: int = Form(...),
    photoUrl: str = Form("")
):
    restaurant = RestaurantCreate(
        name=name,
        category=category,
        city=city,
        price=price,
        photoUrl=photoUrl or None
    )

    restaurant_service.create_restaurant(restaurant)

    return RedirectResponse(
        url="/restaurants",
        status_code=303
    )


# Mostrar formulario para editar
@router.get("/restaurants/{restaurant_id}/edit")
async def edit_restaurant(request: Request, restaurant_id: str):
    restaurant = restaurant_service.get_restaurant(restaurant_id)

    if restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    return templates.TemplateResponse(
        request=request,
        name="restaurant_form.html",
        context={
            "title": "Editar restaurante",
            "action": f"/restaurants/{restaurant_id}/edit",
            "restaurant": restaurant
        }
    )


# Guardar cambios del restaurante
@router.post("/restaurants/{restaurant_id}/edit")
async def update_restaurant(
    restaurant_id: str,
    name: str = Form(...),
    category: str = Form(...),
    city: str = Form(...),
    price: int = Form(...),
    photoUrl: str = Form("")
):
    restaurant = RestaurantUpdate(
        name=name,
        category=category,
        city=city,
        price=price,
        photoUrl=photoUrl or None
    )

    updated = restaurant_service.update_restaurant(
        restaurant_id,
        restaurant
    )

    if updated is None:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    return RedirectResponse(
        url="/restaurants",
        status_code=303
    )


# Eliminar restaurante
@router.post("/restaurants/{restaurant_id}/delete")
async def delete_restaurant(restaurant_id: str):
    deleted = restaurant_service.delete_restaurant(restaurant_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Restaurante no encontrado")

    return RedirectResponse(
        url="/restaurants",
        status_code=303
    )
