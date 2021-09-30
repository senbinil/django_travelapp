from django.db import models
from django.db.models.base import Model

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=240)
    title=models.TextField()
    img=models.ImageField(upload_to='uploads/')

    def __str__(self) -> str:
        return self.name
class News(models.Model):
    date=models.IntegerField()
    post_title=models.CharField(max_length=240)
    content=models.CharField(max_length=240)
    image=models.ImageField(upload_to='uploads/')
    image.blank=True
