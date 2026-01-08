from django.urls import path
from .views import *

urlpatterns = [
    path('', reviewsPage, name='reviews'),
]