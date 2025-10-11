from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    
    category_name = models.CharField(max_length=100, unique=True)
    category_slug = models.SlugField(max_length=100, unique=True , auto_created=True) ##nothing but url
    category_description = models.TextField(max_length=200 , blank=True) #blank=True means its not mandatory
    category_img = models.ImageField(upload_to='photos/category/') #blank=True means its not mandatory
    category_created_date = models.DateTimeField(auto_now_add=True)
    category_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories" ##just to make plural form of category in admin panel

    def get_url(self):
        return reverse('products_by_category' , args = [self.category_slug])  ##to make dynamic url for each category

    
    def __str__(self):
        return self.category_name