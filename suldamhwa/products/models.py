from django.db    import models
from users.models import User
from core.models  import TimeStampModel

class Product(models.Model):
    size               = models.IntegerField()
    name               = models.CharField(max_length=100)
    description_detail = models.CharField(max_length=1000)
    description_tag    = models.CharField(max_length=1000)
    price              = models.DecimalField(max_digits=8, decimal_places=2)
    category           = models.ForeignKey('Category', on_delete=models.CASCADE)
    alcohol_percentage = models.DecimalField(max_digits=3, decimal_places=1)
    alcohol_type       = models.ForeignKey('AlcoholType', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    image_url = models.URLField(max_length=2000)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

class CategoryImage(models.Model):
    image_url = models.URLField(max_length=2000)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category_images'

class Comment(TimeStampModel):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    class Meta:
        db_table = 'comments'

class AlcoholType(models.Model):
    type  = models.CharField(max_length=100)

    class Meta:
        db_table = 'alcohol_types'

class FingerFood(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'finger_foods'

class FingerFoodImage(models.Model):
    image_url   = models.URLField(max_length=2000)
    finger_food = models.ForeignKey(FingerFood, on_delete=models.CASCADE)

    class Meta:
        db_table = 'finger_food_images'

class OrderItem(TimeStampModel):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    product    = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    count      = models.PositiveIntegerField()
    price      = models.DecimalField(max_digits=8, decimal_places=2)
    is_checked = models.BooleanField(default=True)
    order      = models.ForeignKey("Order", on_delete=models.CASCADE)

    class Meta:
        db_table = 'orderitems'

class Order(TimeStampModel):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    address      = models.CharField(max_length=1000)
    order_status = models.ForeignKey("OrderStatus", on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"

class OrderStatus(models.Model):
    status = models.CharField(max_length=1000)

    class Meta:
        db_table = "order_status"

class Taste(models.Model):
    spiceness       = models.IntegerField()
    savory          = models.IntegerField()
    refreshness     = models.IntegerField()
    taste_intensity = models.IntegerField()
    sweetness       = models.IntegerField()
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "tastes"