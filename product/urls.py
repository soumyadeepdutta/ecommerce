from django.urls import path
from .views import ProductList, ProductDetail

app_name = 'product'
urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('details/<int:pk>', ProductDetail.as_view(), name='detail')
]
