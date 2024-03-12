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
Creating a Virtual Environment: Create a virtual environment named BeautySalon.

     python -m venv myprojectenv
     
Activate the virtual environment:

    ●	On macOS/Linux: source myprojectenv/bin/activate
    ●	On Windows: myprojectenv\Scripts\activate
    
Installing Django and Django Rest Framework: Install Django and DRF using pip.

    ●	pip install django
    ●	pip install djangorestframework
    
Creating a Django Project: Generate a new Django project.

    ●	django-admin startproject myproject
    
Replace BeautySalon with your desired project name. Running the Django Server
Navigate to your project directory and start the Django server.

    ●	cd BeautySalon
    ●	pip install psycopg2
    ●	pip install psycopg2-binary
    ●	python manage.py runserver
    
*pgadmin create database

We move to the folder that has the project

    * python3 manage.py runserver
    
In Django, an application is a web application that does something – a self-contained feature or functionality of your project. Think of it as a specific district or neighborhood within our city, dedicated to a particular purpose, like residential, commercial, or industrial. Create your first app with:

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
        'NAME': 'beautysalondatabase',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
      }
    }
__________________________________________________________________________________________________________________

To create a REST API endpoint based on the specifications and code you provided, we'll integrate the Django models, serializers, and views into a Django project. Here's a step-by-step guide:

1. Set up a Django project:

If you haven't already, install Django (pip install django) and create a new project 
(django-admin startproject myproject).
Navigate into the project directory (cd myproject).

2. Create Django apps:

Inside the project directory, create a new Django app (django-admin startapp myapp).
This app will contain the models, serializers, views, and URLs for your REST API.

3. Models:

Copy the model definitions from your provided code and paste them into models.py inside 
your app directory (myproject/myapp/models.py).

    from django.db import models

    class Client(models.Model):
      name = models.CharField(max_length=100)
      phone = models.CharField(max_length=15)
      email = models.EmailField()

    class Service(models.Model):
      name = models.CharField(max_length=100)
      description = models.TextField()
      price = models.DecimalField(max_digits=10, decimal_places=2)
      details = models.JSONField()

    class Appointment(models.Model):
      client = models.ForeignKey(Client, on_delete=models.CASCADE)
      service = models.ForeignKey(Service, on_delete=models.CASCADE)
      date = models.DateField()
      time = models.TimeField()
      additional_info = models.JSONField(blank=True, null=True)

    class Booking(models.Model):
      appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
      payment_status = models.BooleanField(default=False)

    class UploadedFile(models.Model):
      file = models.FileField(upload_to='uploads/')
      uploaded_at = models.DateTimeField(auto_now_add=True)

4. Serializers:

Copy the serializer definitions from your provided code and paste them into 
serializers.py inside your app directory (myproject/myapp/serializers.py).

    from rest_framework import serializers
    from .models import Client, Service, Appointment, Booking, UploadedFile

    class ClientSerializer(serializers.ModelSerializer):
      class Meta:
        model = Client
        fields = '__all__'

    class ServiceSerializer(serializers.ModelSerializer):
      class Meta:
        model = Service
        fields = '__all__'

    class AppointmentSerializer(serializers.ModelSerializer):
      class Meta:
        model = Appointment
        fields = '__all__'

    class BookingSerializer(serializers.ModelSerializer):
      class Meta:
        model = Booking
        fields = '__all__'

    class UploadedFileSerializer(serializers.ModelSerializer):
      class Meta:
        model = UploadedFile
        fields = '__all__'

5. Views:

Copy the view functions and classes from your provided code and paste them into 
views.py inside your app directory (myproject/myapp/views.py).

    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from rest_framework import status
    from .models import Client, Service, Appointment, Booking
    from .serializers import ClientSerializer, ServiceSerializer, AppointmentSerializer, BookingSerializer, UploadedFileSerializer

    @api_view(['GET', 'POST'])
    def client_list(request):
      if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

6. URLs:

Copy the URL patterns from your provided code and paste them into urls.py inside your 
app directory (myproject/myapp/urls.py).
Ensure you import the necessary views (from . import views) at the top of the file.

    from django.urls import path
    from . import views

    urlpatterns = [
       path('clients/', views.client_list),
       path('services/', views.service_list),
       path('appointments/', views.appointment_list),
       path('bookings/', views.booking_list),
       path('files/', views.uploaded_file_list),
    ]

7. Settings:

In your project's settings.py, add your app to the INSTALLED_APPS list ('myapp').
Make sure your project's urls.py includes your app's URLs. You might include them using 
the include function (path('api/', include('myapp.urls'))).

# Package installations
    pip install django djangorestframework django-filter django-rest-swagger boto3 django-storages psycopg2-binary

# Git configuration
    git config --global user.name "Tu Nombre"
    git config --global user.email “tucorreo@example.com”

# Creating the local repository
    mkdir BeautySalonAPI
    cd BeautySalonAPI
    git init

# # Creating the virtual environment
    python -m venv myprojectenv
    source myprojectenv/bin/activate  # Linux / macOS
    myprojectenv\Scripts\activate  # Windows

# Installing Django and Django Rest Framework
    pip install django djangorestframework django-filter django-rest-swagger boto3 django-storages psycopg2-binary

# Creating the Django project
    django-admin startproject BeautySalonAPI

# Changing to the project directory
    cd BeautySalonAPI

# Creating a new application
    python manage.py startapp BeautySalonApp

8. Run Migrations:

Run python manage.py makemigrations and python manage.py migrate to apply the 
model changes to your database.

9. Test the API:

Start your Django development server with python manage.py runserver.
Use tools like Insomnia or Postman to interact with your API endpoints.
Follow the instructions provided in the "Using Insomnia" section to authenticate and make 
requests to your API endpoints.

10. Integrate AWS S3 (Optional):

If you want to integrate AWS S3 for file storage, follow the steps provided under the "Implementing AWS S3 with Django" section.
Make sure to install the required packages (django-storages and boto3) and configure your settings accordingly.]

11. Implement Throttling and Permissions (Optional):

If you want to implement throttling and permissions as described in the provided code, follow the instructions under the 
"Implementing Throttling in Django REST Framework (DRF)" section.

12. Implement Pagination (Optional):

If you want to implement pagination as described in the provided code, follow the instructions 
under the "Implementing Pagination in Django REST Framework (DRF)" section.
