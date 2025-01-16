# DRF Task

This is a Django REST Framework application for managing blogs and comments.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/neer-aubergine/DRF_Task
cd DRF_Task
```

### 2. Create and activate a virtual environment (optional but recommended)

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```
### 4. Set up the database

```sh
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a superuser

```sh
python manage.py createsuperuser
```
### 6. Add sample data (using Faker) -- OPTIONAL

```sh
python manage.py poplate_db
```
### 7. Run the development server

```sh
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000/`.


### 8. Install djago-silk for live inspection/optimization of DRF -- OPTIONAL

```sh
pip install django-silk
```

In `settings.py` add the following:

```python
MIDDLEWARE = [
    ...
    'silk.middleware.SilkyMiddleware',
    ...
]

INSTALLED_APPS = (
    ...
    'silk'
)
```
To enable access to the user interface add the following to your `urls.py`:

```python
urlpatterns = [
    ...
    path('silk/', include('silk.urls', namespace='silk'))
    ...
    ]
```

before running migrate:

```bash
python manage.py migrate

python manage.py collectstatic
```


Silk will automatically begin interception of requests and you can proceed to add profiling
if required. The UI can be reached at `/silk/`

For more custumizations [Django-Silk](https://github.com/jazzband/django-silk)




## Features

- [x] Register & login using Email & Password using JWT
- [x] User profile updation
- [x] Blogs CRUD functionality (Create, Read, Update, Delete)
- [x] Support of filters by Author, Category, and Tags 
- [x] Route protection
- [x] Pagination for list of blogs
- [x] Support of filters by a textual search parameter
- [x] Comment count for each blog
- [x] All users should be able to add comments to a blog published by anyone on the platform
- [x] Author can delete anyone’s comment on a self-published blog
- [x] Used Faker to populate db
- [ ] Email notification to a blog publisher when someone else puts a comment on the blog

