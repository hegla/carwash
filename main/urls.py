from django.urls import path
from main import views as views


app_name = 'main'
urlpatterns = [
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer'),
    path('customers', views.CustomerListView.as_view(), name='customers'),
    path('customer/create', views.CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/update', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete', views.CustomerDeleteView.as_view(), name='customer-delete')
]