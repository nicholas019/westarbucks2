from django.db import models
from menu.models import Menu

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=45)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"

