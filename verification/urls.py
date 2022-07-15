from django.urls import path

from .views import VerificationViewSet

urlpatterns = [
    path('verification', VerificationViewSet.as_view({
        'post': 'create',
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]