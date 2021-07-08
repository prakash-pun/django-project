# django-project
## To Run the application

```
> virtualenv venv
> venv\Scripts\activate
> pip install -r requirements.txt
```

- create `social_settings.py` on `mysite` folder i.e. `mysite/github_settings.py` and add the following
```
SOCIAL_AUTH_GITHUB_KEY = 'your key'
SOCIAL_AUTH_GITHUB_SECRET = 'your secret key'
```

```
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver
```

`happy coding 😁`
