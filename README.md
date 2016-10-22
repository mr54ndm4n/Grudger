# Grudger

Grudger is Online Judge for Online Programming Class
Using
- Python 3.5.2 *(Programming Language)*
- Django 1.10.2 *(Web Framework)*

## to Install Grudger
**If You're using Linux for server then delete grader/views.py and rename grader/views_for_linux.py to grader/views.py (Replace)*
- Clone [Grudger](https://github.com/DreamN/Grudger.git)

	```
		$git clone https://github.com/DreamN/Grudger.git
	```
- Install [PIP](https://pypi.python.org/pypi/pip)
- Install Django

	```
		$pip install Django==1.10.2
	```
- Create local_settings.py
	```
	Grudger/
		Grudger/
			__init__.py
			local_settings.py
			settings.py
			urls.py
			views.py
			wsgi.py
		grader/
		templates/
		.gitignore
		manage.py
		requirements.txt
		runtime.txt
	```
	and paste and code below on local_settings.py and edit for your database then save!
	```python
	import os

	# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	# Database
	# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
	    in local_settings.py
	        DATABASES = {
	            'default': {
	                'ENGINE': 'django.db.backends.postgresql',
	                'NAME': 'mydatabase',
	                'USER': 'mydatabaseuser',
	                'PASSWORD': 'mypassword',
	                'HOST': '127.0.0.1',
	                'PORT': '5432',
	            }
	        }
	```
- Make Migrations

```
$ python manage.py makemigrations
```
- Migrate

```
$ python manage.py migrate
```
- Create Superuser (for access site/admin)

```
$ python manage.py createsuperuser
```

**[Django Deployment Checklist](https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/)*

### Run Server
```
$ python manage.py runserver
```
