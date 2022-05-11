from django.db import models
from category.models import Category
from allergy.models import Allergy



class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    allergydrink = models.ManyToManyField(Allergy, through="Allergy_Drink")

    class Meta:
        db_table = "drink"


class Allergy_Drink(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_drink"

