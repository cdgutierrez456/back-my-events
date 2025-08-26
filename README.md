# MyEvents Backend
Descripción
API RESTful para la gestión de eventos y usuarios. Desarrollada con FastAPI y SQLAlchemy,
siguiendo principios de arquitectura limpia y responsabilidad única.

##  🚀 Características
- 🔐 API RESTful con FastAPI
- 🧾 PostgreSQL como motor de base de datos
- 👥 Autenticación con JWT
- ⚙️ ORM con SQLAlchemy (Async)
- 🗃️ Alembic para migraciones
- ✅ Documentación Swagger
- 🔄 Despliegue en servidor EC2

## 📁 Estructura del proyecto
/api            → Rutas agrupadas por entidad
/models         → Modelos de SQLAlchemy
/schemas        → Schemas de Pydantic
/services       → Lógica de negocio
/core           → Configuración global
/utils          → Funciones auxiliares
/alembic        → Migraciones

## 🧑‍💻 Requisitos
• Python 3.11+
• PostgreSQL
• pip
• .env configurado

## Variables de entorno
DATABASE_URL=postgresql+asyncpg://user:password@host:port/dbname
SECRET_KEY=clave_secreta
ALGORITHM=HS256

## Instalación
git clone https://github.com/cdgutierrez456/back-my-events.git
cd back-my-events
- Linuz/Mac: source venv/bin/activate
- Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

## Tests
En desarrollo. Se planea integrar pytest, pytest-asyncio y coverage.py

## Despliegue
Aunque la dockerización está pendiente, el backend está desplegado funcionalmente en:
https://api.myeventtest.lat/docs

## API Documentada
Incluye endpoints para login, usuarios, eventos, perfiles y permisos. Toda la API está documentada
automáticamente en Swagger.

## Repositorio Frontend
https://github.com/cdgutierrez456/front-my-events

## Autor
Cristian David Gutiérrez
Desarrollador Fullstack
GitHub: https://github.com/cdgutierrez456