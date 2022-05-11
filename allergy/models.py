from django.db import models

# Create your models here.

class Allergy(models.Model):
    allergy_name = models.CharField(max_length=45)

    class Meta:
        db_table = "allergy"
