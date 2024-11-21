from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(ProductCategory, related_name='products')

    def __str__(self):
        return self.name


class Basket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='active')

    def __str__(self):
        return f"Basket {self.id} - {self.status}"


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='basket_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
