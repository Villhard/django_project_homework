from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products")


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __repr__(self):
        return f"Category(name={self.name}, description={self.description})"

    def __str__(self):
        return self.name
