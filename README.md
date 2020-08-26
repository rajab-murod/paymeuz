## Introduction

this package helps to integrate [payme.uz](http://payme.uz) and your application is built on django.

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

PAYMEUZ_SETTINGS = {
  'DEBUG' : True   # True - test, False - production.
  'MERCHANT_ID' : '',
  'SECRET_KEY' : '',
  'ACCOUNTS' : {
    'KEY_1' : '',
    'KEY_2' : ''
  }
}

# urls.py

urlpatterns = [
    ...
    path('api/payme/',include('paymeuz.urls'))
]
```
