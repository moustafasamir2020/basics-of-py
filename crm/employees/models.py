from django.db import models

# Create your models here.
class employee (models.Model):
    name=models.CharField( max_length=250)
    age=models.IntegerField()
    salary=models.FloatField()

    def __str__(self):
        return self.name
    