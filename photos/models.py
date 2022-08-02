from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class image(models.Model):
    name = models.TextField()
    image = CloudinaryField('image',blank=True,null=True)
    description = models.TextField()
    location = models.TextField()