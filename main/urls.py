from django.urls import path
from main import views as views


app_name = 'main'

urlpatterns = [
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customer/create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('customer/<int:pk>/update/', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer-delete'),
    path('carwashes/', views.CarwashListView.as_view(), name='carwashes'),
    path('map/', views.CarwashMapView.as_view(), name='map'),
    path('carwash/create/', views.CarwashCreateView.as_view(), name='carwash-create'),
    path('carwash/<int:pk>/', views.CarwashDetailView.as_view(), name='carwash'),
    path('carwash/<int:pk>/update/', views.CarwashUpdateView.as_view(), name='carwash-update'),
    path('carwash/<int:pk>/delete/', views.CarwashDeleteView.as_view(), name='carwash-delete'),
    path('carwashes/carwash-search/', views.carwash_autocomplete, name='carwash-search'),
    path('orders/', views.OrderListView.as_view(), name='orders'),    
    path('order/create/', views.OrderCreateView.as_view(), name='order-create'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order-delete'),
    path('customer-autocomplete/', views.CustomerAutocomplete.as_view(), name='customer-autocomplete'),
    path('carwash-autocomplete/', views.CarwashAutocomplete.as_view(), name='carwash-autocomplete'),
    path('map_data/<int:pk>/', views.map_data, name='map-data'),
]