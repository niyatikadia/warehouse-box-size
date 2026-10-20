from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    length = models.FloatField()   # cm
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()   # kg
    is_fragile = models.BooleanField(default=False)

class Box(models.Model):
    name = models.CharField(max_length=200)
    internal_length = models.FloatField()
    internal_width = models.FloatField()
    internal_height = models.FloatField()
    max_weight = models.FloatField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)