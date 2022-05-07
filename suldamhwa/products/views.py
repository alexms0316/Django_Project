import json, re

from django.shortcuts import render

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from products.models  import Product, ProductImage, Category, CategoryImage, Comment, AlcoholType, FingerFood, FingerFoodImage, OrderItem, Taste
from users.decorator  import log_in_decorator


class ProductListView(View):
    def get(self, request):
        try:
            category_id = request.GET.get('categoryId', None)
            searching   = request.GET.get('productName', None)
            offset      = request.GET.get('offset', 0)
            limit       = request.GET.get('limit', 30)

            filter_condition = Q()

            if category_id:
                filter_condition &= Q(category_id=category_id)

            if searching:
                filter_condition &= Q(name__icontains=searching)

            products = Product.objects.filter(filter_condition).order_by('?')[offset:offset+limit]

            product_list = [{
                'category_id'     : product.category.id,
                'product_id'      : product.id,
                'name'            : product.name,
                'price'           : product.price,
                'description_tag' : product.description_tag,
                'products_image'  : product.productimage_set.first().image_url,
            } for product in products]

            return JsonResponse({'product_list' : product_list}, status = 200)

        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status = 400)