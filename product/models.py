from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "categories"
    name = models.CharField(max_length=20, null=False)
    menu = models.CharField(max_length=20, null=False)

class Drink(models.Model):
    class Meta:
        db_table = "drinks"

    name = models.CharField(max_length=20, null=False)
    nut_info = models.CharField(max_length=256, null=False)
    allergic = models.CharField(max_length=256, null=False)
    category = models.ManyToManyField(Category)

