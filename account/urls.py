from django.urls import path
from .views import *

urlpatterns = [
    path('', first, name='first'),
    path('login/',login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("register/", register_view, name="signup"),
]
