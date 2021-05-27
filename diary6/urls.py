from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('list1/', list1, name="list1"),
    path('<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name='delete'),
]
