from django.urls import path
from .views import simple_api_view

urlpatterns = [
    path('', simple_api_view, name='simple'),
]