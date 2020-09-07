from django.urls import path
from main import views as views


app_name = 'main'
urlpatterns = [
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer'),
]