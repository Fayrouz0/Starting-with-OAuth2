from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.home, name=""),

    path('register',views.register, name="register"),

    path('login',views.login, name="login"),

    path('dashboard',views.dashboard, name="dashboard"),
    
    #path('google/login',views.login,name='provider_login_google')
]