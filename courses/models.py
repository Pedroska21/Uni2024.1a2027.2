from django.db import models
from django.core.validators import FileExtensionValidator
from episodes.models import Episodes

class Category(models.Model):
    title = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=255)
    hours = models.IntegerField()
    description = models.CharField(max_length=255)
    banner = models.FileField(upload_to='uploads/banners', validators= [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    episode = models.ManyToManyField(Episodes)
    
