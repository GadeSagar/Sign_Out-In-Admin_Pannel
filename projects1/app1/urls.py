from django.urls import path
from . import views

app_name = 'app1'          # here for namespacing of urls

urlpatterns = [
    #path("", views.homepage, name = "homepage"),
    path("user_login", views.user_login,name='user_login'),
    path("register", views.register, name = "register"),
    #path("logout", views.logout_register, name = "logout"),
]