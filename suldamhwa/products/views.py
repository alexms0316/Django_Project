import json, re

from json.decoder     import JSONDecodeError

from django.shortcuts import render

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from users.models     import User
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

class CommentView(View):
    @log_in_decorator
    def post(self, request, product_id):
        try:
            data         = json.loads(request.body)
            user         = request.user
            content      = data.get('content', None)

            if not Product.objects.filter(id=product_id).exists():
                return JsonResponse({'message': 'PRODUCT_DOES_NOT_EXIST'}, status=404)

            Comment.objects.create(
                content    = content,
                user       = user,
                product_id = product_id
                )

            return JsonResponse({'message':'SUCCESS'}, status=201)

        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)

    def get(self, request, product_id):
        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'message':'COMMENT_DOES_NOT_EXIST'}, status=404)

        comment_list = [{
            "name"  : User.objects.get(id=comment.user.id).name,
            "content"   : comment.content,
            "create_at" : comment.created_at
            } for comment in Comment.objects.filter(product_id=product_id)
        ]

        return JsonResponse({'data':comment_list}, status=200)

    @log_in_decorator
    def delete(self, request, product_id, comment_id):
        user_id    = request.user.id
        product_id = product_id

        if not Comment.objects.filter(id=comment_id, product_id=product_id, user_id=user_id).exists():
            return JsonResponse({'message':'COMMENT_DOES_NOT_EXIST'}, status=404)

        Comment.objects.filter(id=comment_id, product_id=product_id, user_id=user_id).first().delete()
        return JsonResponse({'message': 'SUCCESS'}, status=204)

class SubscribeView(View):
    def get(self, request, product_id):
        try:
            products = Product.objects.filter(id = product_id)

            subscribe_detail = [({
                'id'                 : product.id,
                'name'               : product.name,
                'product_image'      : product.productimage_set.first().image_url,
                'description_detail' : product.description_detail,
                'price'              : product.price,
                'alcohol_percentage' : product.alcohol_percentage,
                'description_tag'    : product.description_tag,
                'taste'              : [{
                    'id'              : taste.id,
                    'spiceness'       : taste.spiceness,
                    'savory'          : taste.savory,
                    'refreshness'     : taste.refreshness,
                    'taste_intensity' : taste.taste_intensity,
                    'sweetness'       : taste.sweetness
                    } for taste in product.category.taste_set.all()]
            })for product in products]

        except Product.DoesNotExist:
            return JsonResponse({'message':'PRODUCT_DOES_NOT_EXIST'}, status = 404)
        return JsonResponse({
            "message" : 'Subscribe_detail',
            'subscribe_detail': subscribe_detail
            },
            status = 200)