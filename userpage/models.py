from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Upload(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField()
    description=models.CharField(max_length=250)
