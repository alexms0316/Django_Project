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

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            products = Product.objects.filter(id = product_id)

            product_detail = [{
                'id'                 : product.id,
                'size'               : product.size,
                'name'               : product.name,
                'description_detail' : product.description_detail,
                'description_tag'    : product.description_tag,
                'price'              : product.price,
                'alcohol_percentage' : product.alcohol_percentage,
                'category'           : product.category.name,
                'product_image'      : [{
                    'id' : product_image.id,
                    'image_url' : product_image.image_url
                    } for product_image in product.productimage_set.all()],
                'taste'              : [{
                    'id'              : taste.id,
                    'spiceness'       : taste.spiceness,
                    'savory'          : taste.savory,
                    'refreshness'     : taste.refreshness,
                    'taste_intensity' : taste.taste_intensity,
                    'sweetness'       : taste.sweetness
                    } for taste in product.category.taste_set.all()],
                'finger_food'        : [{
                    'id'        : finger_food.id,
                    'name'      : finger_food.name,
                    'image_url' : finger_food.image_url
                    } for finger_food in product.category.fingerfood_set.all()]
            } for product in products]

        except Product.DoesNotExist:
            return JsonResponse({'message':'PRODUCT_DOES_NOT_EXIST'}, status = 404)
        return JsonResponse({
            "message" : "product_detail",
            "product_detail": product_detail
            },
            status = 200)
