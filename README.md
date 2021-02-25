# Django-Rest-Framework

### Token Generate :
- python manage.py drf_create_token your_username
- pip install httpie
## Token generate using custom user
- http POST http://127.0.0.1:8000/URL/ username="max" password="yourpassword"

## Data BASE:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "upayfork",
        "USER" : "postgres",
        "PASSWORD" : "alienide",
        "HOST" : "localhost",
        "PORT": "",
    },
}
