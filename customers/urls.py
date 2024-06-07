from django.urls import path

from customers.views import CustomerListView, CustomerCreateView, CustomerDetailView, CustomerUpdateView, \
    CustomerDeleteView

app_name = 'customers'

urlpatterns = [
    path('list/', CustomerListView.as_view(), name='customer_list'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('view/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('edit/<int:pk>/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
]