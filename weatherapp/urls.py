from django.urls import path
from weatherapp import views  # Import the home view


urlpatterns = [
    path('', views.home),
]