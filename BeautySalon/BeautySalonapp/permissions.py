from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class CanViewClients(BasePermission):
    def has_permission(self, request, view):
      
        return request.user.has_perm('yourapp.view_client')

class CanAddService(BasePermission):
    def has_permission(self, request, view):
       
        return request.user.has_perm('yourapp.add_service')
 
class MyPermission(IsAuthenticated):
    pass



class MyPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size' 
