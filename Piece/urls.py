from django.urls import path
from .views import PostCreate

urlpatterns = [
    path('create', PostCreate, name='post-create' ),
]