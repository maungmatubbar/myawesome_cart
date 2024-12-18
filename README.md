1. Install Django-> pip install django
2. Django Admin-> django-admin startproject project_name
3. Create App: Ecommerce and Blog -> python manage.py startapp project_name
4. Migrate -> python manage.py migrate
5. Make Migration -> python manage.py makemigrations
6. Show all Migration files-> python manage.py showmigrations
7. Code run shell-> python manage.py shell
8. Create Super User-> python manage.py createsuperuser
9. Media File Add -> settings-> import os
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR,'media')
  *urls.py-> [] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
