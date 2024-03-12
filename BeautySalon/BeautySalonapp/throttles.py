from rest_framework.throttling import AnonRateThrottle

class CustomAnonRateThrottle(AnonRateThrottle):
    def authenticate(self, request, view):
        # Implementa la lógica de autenticación si es necesario
        return None
