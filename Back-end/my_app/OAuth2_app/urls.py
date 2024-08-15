from django.urls import include,path
from . import views
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('',views.home, name=""),

    path('register',views.register, name="register"),

    path('login',views.login, name="login"),

    path('dashboard',views.dashboard, name="dashboard"),
    
    path('o/', include(oauth2_urls)),

]