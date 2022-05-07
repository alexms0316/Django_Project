from django.urls import path
from products.views import ProductListView, ProductDetailView, CommentView, SubscribeView

urlpatterns = [
    path('/list', ProductListView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/<int:product_id>/comment', CommentView.as_view()),
    path('/<int:product_id>/comment/<int:comment_id>', CommentView.as_view()),
    path('/<int:product_id>/subscribe', SubscribeView.as_view())
    ]