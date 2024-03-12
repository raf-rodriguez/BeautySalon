from rest_framework.throttling import UserRateThrottle

class MyThrottle(UserRateThrottle):
    rate = '5/minute'  # Permite 5 solicitudes por minuto por usuario
