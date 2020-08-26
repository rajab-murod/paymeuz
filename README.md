## Introduction

this package helps to integrate [payme.uz](http://payme.uz) and your application is built on [django](https://www.djangoproject.com/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install requests
pip install djangorestframework
pip install paymeuz
```

## Usage

```python
# settings.py

INSTALLED_APPS = [
     ... 
    'paymeuz',
    'rest_framework',
     ...
]

PAYME_SETTINGS = {
    'DEBUG':True,   #True - test, False - production
    'ID':'',  
    'SECRET_KEY':'',
    'ACCOUNTS':{
        'KEY_1':'order_id',
        'KEY_2':'',
    }
}

# urls.py

urlpatterns = [
    ...
    path('api/payme/',include('paymeuz.urls'))
]
```

## Get started
```bash
python manage.py migrate
python manage.py runserver
```

## Documentation
 - payme.uz [docs](https://help.paycom.uz/ru/metody-subscribe-api)
 - django-rest-framework [docs](https://www.django-rest-framework.org/)
