from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('', views.index, name='home_page'),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/', profile, name='profile'),
    path('laboratory_seven/', laboratory_seven, name='lab7'),
    path('create_record/', create_record, name='create_record'),
    path('delete_record/<int:el_id>', delete_rec, name='delete_rec'),
    path('update_record/<int:pk>/', UpdateRecord.as_view(), name='update_record'),
]