
# FriendlyEats FastAPI

## Descripción
Aplicación web para promocionar restaurantes de una ciudad, permitiendo a los usuarios consultar información y conocer diferentes opciones gastronómicas.

## Objetivo del Sprint 1
Crear una aplicación local que permita registrar, consultar, editar y eliminar restaurantes utilizando FastAPI y Firebase Firestore.

## Tecnologías
- Python
- FastAPI
- HTML
- CSS
- JavaScript
- Jinja2
- Firebase Firestore Emulator
- Git
- Pytest

## Funcionalidades desarrolladas
- Registro de restaurantes.
- Consulta de todos los restaurantes.
- Consulta de detalles de un restaurante.
- Edición de restaurantes.
- Eliminación de restaurantes.
- Filtro por ciudad.
- Filtro por categoría.
- Filtro por precio.
- Interfaz web con plantillas HTML.

## Estructura del proyecto
- app/: código principal de la aplicación.
- app/api/: rutas de la aplicación.
- app/core/: configuración y conexión con Firestore.
- app/domain/: esquemas de datos.
- app/repositories/: operaciones con la base de datos.
- app/services/: lógica de los restaurantes.
- app/templates/: páginas HTML.
- static/: archivos CSS, JavaScript e imágenes.
- tests/: pruebas automáticas.

## Ejecución del proyecto

### 1. Activar el entorno virtual
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Iniciar Firestore Emulator
```bash
firebase emulators:start --only firestore --project friendlyeats-local
```

### 3. Iniciar FastAPI
```bash
uvicorn app.main:app --reload
```

### 4. Abrir la aplicación
http://127.0.0.1:8000

### 5. Documentación de la API
http://127.0.0.1:8000/docs

## Pruebas automáticas
Para ejecutar las pruebas:

```bash
python -m pytest -v
```

Actualmente se tienen 3 pruebas aprobadas:
- Creación de restaurante.
- Actualización de restaurante.
- Validación de precio.

## Estado del proyecto
Sprint 1: desarrollo de la aplicación local, conexión con Firestore Emulator, operaciones CRUD, filtros y pruebas automáticas.
