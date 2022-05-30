from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path("signup",views.sign_up,name='signup'),
    path("contacts",views.contact,name='contact'),
    path("login",views.login,name='login'),
    path("",views.index,name='home'),
    path("main",views.main_page,name='main'),
    path("decod",views.decode,name='decod_txt'),
    
    # path("video_trim",views.video_trim,name='trim'),
    # path("helo",views.helo,name='helo'),
    
]
