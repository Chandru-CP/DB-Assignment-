from django.db import models

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProductInventory(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    SKU = models.CharField(max_length=50)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,null=False)  # Many-to-one relationship with ProductCategory
    inventory_id = models.OneToOneField(ProductInventory, on_delete=models.CASCADE,null=False)  # One-to-one relationship with ProductInventory
    price = models.DecimalField(max_digits=10, decimal_places=3)
    discount_id = models.ForeignKey(Discount, on_delete=models.CASCADE,null=False)  # Many-to-one relationship with Discount
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
