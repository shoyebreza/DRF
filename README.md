
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



