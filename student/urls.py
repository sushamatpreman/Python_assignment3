from django.urls import path
from.import views

urlpatterns = [
    path('',views.register,name='register'),
    path('logi/',views.login,name='log'),
   
]