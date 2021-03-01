from django.db import models

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="pic")
    price = models.IntegerField()
    desc = models.TextField()
    offer = models.BooleanField(default=False)

class feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    message =  models.TextField()




