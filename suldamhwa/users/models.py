from django.db import models

class User(models.Model):
    email      = models.CharField(max_length=100, unique=True)
    password   = models.CharField(max_length=200)
    name       = models.CharField(max_length=30)
    nick_name  = models.CharField(max_length=45, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
