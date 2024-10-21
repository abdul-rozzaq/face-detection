from django.urls import path
from .views import recognize, home_page, user_login, user_logout, register


urlpatterns = [
    path("", home_page, name="home"),

    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),

    path("recognize/", recognize),
]
