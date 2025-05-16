from django.db import models
from category.models import Category
from django.shortcuts import redirect

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    sku = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/images', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    is_deleted = models.BooleanField(default=False)

    @classmethod
    def getall(cls):
        return cls.objects.filter(is_deleted=False)

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def Add(cls, name, description, price, stock, sku, image, category):
        return cls.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            sku=sku,
            image=image,
            category=category
        )

    @classmethod
    def update(cls, id, name, description, price, stock, sku, image=None, category=None):
        product = cls.objects.get(pk=id)
        product.name = name
        product.description = description
        product.price = price
        product.stock = stock
        product.sku = sku
        if image:
            product.image = image
        if category:
            product.category = category
        product.save()

    @classmethod
    def softdelete(cls, id):
        cls.objects.filter(pk=id).update(is_deleted=True)

    @classmethod
    def harddel(cls, id):
        cls.objects.filter(pk=id).delete()

    @staticmethod
    def go_to_product_list():
        return redirect('product:product_list')

    def __str__(self):
        return self.name


