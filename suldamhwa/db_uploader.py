import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suldamhwa.settings")
django.setup()

from users.models import User
from products.models import Product, Category, ProductImage, CategoryImage, Comment, AlcoholType, FingerFood, FingerFoodImage, OrderItem, Taste


CSV_PATH_CATEGORIES = 'categories.csv'
CSV_PATH_TASTES = 'tastes.csv'
CSV_PATH_CATEGORY_IMAGES = 'category_images.csv'
CSV_PATH_FINGER_FOODS = 'finger_foods.csv'
CSV_PATH_FINGER_FOODS_IMGAES = 'finger_foods_images.csv'
CSV_PATH_ALCOHOL_TYPES = 'alcohol_types.csv'
CSV_PATH_PRODUCTS = 'products.csv'
CSV_PATH_PRODUCT_IMAGES = 'product_images.csv'
CSV_PATH_USERS = 'users.csv'
CSV_PATH_COMMENTS = 'comments.csv'
CSV_PATH_ORDERITEMS = 'orderitems.csv'

# def insert_categories():
with open(CSV_PATH_CATEGORIES) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id   = row[0]
        name = row[1]

        Category.objects.create(
            id   = id,
            name = name
        )

# def insert_tastes():
with open(CSV_PATH_TASTES) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id              = row[0]
        spiceness       = row[1]
        savory          = row[2]
        refreshness     = row[3]
        taste_intensity = row[4]
        sweetness       = row[5]
        category_id     = row[6]

        Taste.objects.create(
            pk              = id,
            spiceness       = spiceness,
            savory          = savory,
            refreshness     = refreshness,
            taste_intensity = taste_intensity,
            sweetness       = sweetness,
            category_id     = category_id
        )

# def insert_category_images():
with open(CSV_PATH_CATEGORY_IMAGES) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id          = row[0]
        image_url   = row[1]
        category_id = row[2]

        CategoryImage.objects.create(
            pk          = id,
            image_url   = image_url,
            category_id = category_id
        )

# def insert_finger_foods():
with open(CSV_PATH_FINGER_FOODS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id          = row[0]
        name        = row[1]
        category_id = row[2]

        FingerFood.objects.create(
            pk          = id,
            name        = name,
            category_id = category_id
        )

# def insert_finger_foods_images():
with open(CSV_PATH_FINGER_FOODS_IMGAES) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id             = row[0]
        image_url      = row[1]
        finger_food_id = row[2]

        FingerFoodImage.objects.create(
            pk             = id,
            image_url      = image_url,
            finger_food_id = finger_food_id
        )

# def insert_alcohol_types():
with open(CSV_PATH_ALCOHOL_TYPES) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id   = row[0]
        type = row[1]

        AlcoholType.objects.create(
            pk   = id,
            type = type,
            )

# def insert_products(): 
with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id                 = row[0]
        size               = row[1]
        name               = row[2]
        description_detail = row[3]
        description_tag    = row[4]
        price              = row[5]
        alcohol_percentage = row[6]
        alcohol_type_id    = row[7]
        category_id        = row[8]

        Product.objects.create(
            pk                 = id,
            size               = size,
            name               = name,
            description_detail = description_detail,
            description_tag    = description_tag,
            price              = price,
            alcohol_percentage = alcohol_percentage,
            alcohol_type_id    = alcohol_type_id,
            category_id        = category_id
        )
            
# def insert_products_images():
with open(CSV_PATH_PRODUCT_IMAGES) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id         = row[0]
        image_url  = row[1]
        product_id = row[2]

        ProductImage.objects.create(
            pk         = id,
            image_url  = image_url,
            product_id = product_id
        )

# def insert_users():
with open(CSV_PATH_USERS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id         = row[0]
        created_at = row[1]
        updated_at = row[2]
        email      = row[3]
        password   = row[4]
        name       = row[5]
        nick_name  = row[6]

        User.objects.create(
            pk         = id,
            created_at = created_at,
            updated_at = updated_at,
            email      = email,
            password   = password,
            name       = name,
            nick_name  = nick_name
        )

# def insert_comments():
with open(CSV_PATH_COMMENTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id         = row[0]
        created_at = row[1]
        updated_at = row[2]
        content    = row[3]
        product_id = row[4]
        user_id    = row[5]

        Comment.objects.create(
            pk         = id,
            created_at = created_at,
            updated_at = updated_at,
            content    = content,
            product_id = product_id,
            user_id    = user_id
        )

# def insert_orderitems():
with open(CSV_PATH_ORDERITEMS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        id         = row[0]
        created_at = row[1]
        updated_at = row[2]
        count      = row[3]
        price      = row[4]
        is_checked = row[5]
        order_id   = row[6]
        product_id = row[7]
        user_id    = row[8]
        OrderItem.objects.create(
            pk         = id,
            created_at = created_at,
            updated_at = updated_at,
            product_id = product_id,
            count      = count,
            price      = price,
            is_checked = is_checked,
            order_id   = order_id,
            user_id    = user_id
        )