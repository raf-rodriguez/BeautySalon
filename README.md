At BeautySalon, we offer a wide range of services and features to meet the needs of our community of beauty lovers.

Basic Requirements
Make sure you have the following packages installed:

    ●	Python (latest version)
    ●	Django (latest version)
    ●	Django Rest Framework

Installation Steps
Configure Git: Set up your Git user name and email.

    ●	git config --global user.name "Your Name"
    ●	git config --global user.email “youremail@example.com”
    
Create a Local Repository: Initialize a local Git repository.

    ●	mkdir example-project
    ●	cd example-project
    ●	git init
    
Dependencies and Virtual Environment
Creating a Virtual Environment: Create a virtual environment named CoreChronicles.

     python -m venv myprojectenv
     
Activate the virtual environment:

    ●	On macOS/Linux: source myprojectenv/bin/activate
    ●	On Windows: myprojectenv\Scripts\activate
    
Installing Django and Django Rest Framework: Install Django and DRF using pip.

    ●	pip install django
    ●	pip install djangorestframework
    
Creating a Django Project: Generate a new Django project.

    ●	django-admin startproject myproject
    
Replace CoreChronicles with your desired project name. Running the Django Server
Navigate to your project directory and start the Django server.

    ●	cd CoreChronicles
    ●	pip install psycopg2
    ●	pip install psycopg2-binary
    ●	python manage.py runserver
    
*pgadmin create database

We move to the folder that has the project

    * python3 manage.py runserver
    
In Django, an application is a web application that does something – a self-contained feature or functionality of your project. Think of it as a specific district or neighborhood within our city, dedicated to a particular purpose, 
like residential, commercial, or industrial. Create your first app with:

    python manage.py startapp myapp
    
Replace myapp with a suitable name for your application. This command creates a new directory with your app’s name, containing the basic files needed to start building your app.
Registering the App and DRF

Update the INSTALLED_APPS list in settings.py to include 'rest_framework' and your app.

    INSTALLED_APPS = [...,
    'rest_framework',
    'myapp',
    ...
    ]
    
Configuring Django to Use PostgreSQL
Update the DATABASES settings in settings.py with your PostgreSQL credentials.

     DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'corechronilesdatabase',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
      }
    }
__________________________________________________________________________________________________________________
