from django.db import models
from utils.models import BaseModel
from ckeditor.fields import RichTextField
from .managers import WebsiteManager

# Create your models here.

class Category(BaseModel):
    title = models.CharField(max_length=31)


    def __str__(self):
        return self.title

class Subcategory(BaseModel):
    title = models.CharField(max_length=31)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.title

class Website(BaseModel):
    url = models.URLField(max_length=31)
    title = models.CharField(max_length=31)
    description = RichTextField(null=True, blank=True)
    position_in_list = models.PositiveIntegerField()
    is_tasix = models.BooleanField(default=False)
    visitors = models.IntegerField()
    views = models.IntegerField()
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='subcategories')
    website_manager = WebsiteManager()

    def __str__(self):
        return self.title





