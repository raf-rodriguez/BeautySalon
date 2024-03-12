from django.urls import path
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from . import views
from .views import AppointmentCreate, UserCreate, ProtectedView, FileUploadView, LoginView
from rest_framework.authtoken.views import obtain_auth_token


# Schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="My Awesome API",
        default_version='v1',
        description="Descripción de mi API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', views.client_list, name='client-list'),
    path('api/token/', obtain_auth_token, name='obtain_auth_token'),
    path('clients/<int:pk>/', views.client_detail, name='client-detail'), 
    path('services/', views.service_list, name='service-list'),
    path('services/<int:pk>/', views.service_detail, name='service-detail'),
    path('appointments/', views.appointment_list, name='appointment-list'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment-detail'),
    path('api/appointments/create/', AppointmentCreate.as_view(), name='create-appointment'),
    path('api/users/register/', UserCreate.as_view(), name='user-create'),
    path('swagger/schema/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/login/', obtain_auth_token, name='login'), 
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('accounts/login/', LoginView.as_view(), name='custom_login'),
]
