from django.urls import path

from .views import VerificationViewSet

urlpatterns = [
    path('verification', VerificationViewSet.as_view({
        'post': 'create'
    })),
    path('verification/<str:pk>', VerificationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]