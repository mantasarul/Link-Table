from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_name}"


class Link(models.Model):
    link_name = models.CharField(max_length=300)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.link_name} {self.category_id} "
    