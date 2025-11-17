from django.urls import path
from greeting import views


urlpatterns = [
  path('', views.home),
  path('about/',views.about)
 
]