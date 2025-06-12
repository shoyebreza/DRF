# Phimart - Ecommerce API (Django REST Framework)

![Django REST Framework](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20token)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)

Phimart is a robust ecommerce API built with Django REST Framework featuring JWT authentication, comprehensive product management, and order processing capabilities.

## Features

- **User Authentication** (JWT via Djoser)
- **Product Management** (CRUD operations)
- **Category System** (Product organization)
- **Shopping Cart Functionality**
- **Order Processing System**
- **Interactive API Documentation** (Swagger/OpenAPI)
- **RESTful API Design**

## API Endpoints


Interactive API documentation available at `/swagger/` and `/redoc/`


## Installation

1. Clone the repository:
```bash
git clone https://github.com/shoyebreza/DRF.git
cd phimart
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
```bash
cp .env.example .env
```
Edit `.env` with your settings (SECRET_KEY, DATABASE_URL, etc.)

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser (optional):
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Authentication**: Djoser with JWT
- **Documentation**: drf-yasg (Swagger/OpenAPI)
- **Database**: PostgreSQL (recommended) / SQLite
- **Other**: SimpleJWT, Django CORS Headers

## Configuration

Important settings in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'djoser',
    'drf_yasg',
    'corsheaders',
    'your_app_name',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

MD. Shoyeb  - shoyebreza@gmail.com

Project Link: [https://github.com/shoyebreza/DRF](https://github.com/shoyebreza/DRF)
















python -m venv .phi_env

cd .phi_env/Scripts/activate

cd ../..

pip list

pip install django

pip install --upgrade pip

django-admin startproject phimart.

pip freeze > requirements.txt

django-admin startapp users

django-admin startapp product

django-admin startapp order

django-admin startapp api

python manage.py runserver

pip install djangorestframework

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

pip install pillow

python -m pip install django-debug-toolbar

python manage.py loaddata fixtures/product_data.json

drf-nested-routers

pip install django-filter

pip install -U djoser

pip install -U djangorestframework_simplejwt

pip install -U drf-yasg

https://drf-yasg.readthedocs.io/en/stable/index.html






