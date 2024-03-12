from django.db import models
from utils.models import BaseModel
from ckeditor.fields import RichTextField
from .managers import WebsiteManager
from users.models import User
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
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='websites')
    website_manager = WebsiteManager()

    def __str__(self):
        return self.url


class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    joined_date = models.DateTimeField()


    # def __str__(self):
    #     return f"{self.user} --> {self.website}"


class View(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    viewed_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.visitor} "






