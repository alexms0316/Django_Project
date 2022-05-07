from django.shortcuts import render

import json, re
import bcrypt, jwt

from django.views           import View
from django.http            import JsonResponse
from django.conf            import settings
from django.core.exceptions import ValidationError

from users.validation import email_validate, password_validate
from users.models     import User

from datetime     import datetime, timedelta
from json.decoder import JSONDecodeError

class SignupView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']

            email_validate(email)
            password_validate(password)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' :'ALREADY_EXISTS_EMAIL'}, status=400)

            hashed_password = bcrypt.hashpw((password).encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                email     = email,
                password  = hashed_password,
                name      = data['name'],
                nick_name = data['nick_name']
                )

            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except ValidationError:
            return JsonResponse({'message':'VALIDATION_ERROR'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)

class EmailValidateView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
            email = data['email']

            email_validate(email)

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' :'ALREADY_EXISTS_EMAIL'}, status=400)

            return JsonResponse({'message':'SUCCESS'}, status=201)
        except ValidationError:
            return JsonResponse({'message':'VALIDATION_ERROR'}, status=400)

class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user = User.objects.get(email=data['email'])

            hashed_password = user.password.encode('utf-8')
            access_token    = jwt.encode({'id':user.id, 'exp':datetime.utcnow() + timedelta(weeks=3)}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), hashed_password):
                return JsonResponse({'message': "INVALID_USER"}, status=401)
            
            return JsonResponse({'message':'SUCCESS', 'token': access_token}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=404)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
