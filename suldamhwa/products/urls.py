from django.urls import path
from products.views import ProductListView, ProductDetailView

urlpatterns = [
    path('/list', ProductListView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    ]