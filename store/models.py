from django.db import models
from product_categories.models import Category
from django.urls import reverse
from django.utils.text import slugify


# Packaging: 1 kg and 25 kg
# Crops: Cereals, pulses, oilseeds, fruits, vegetables, and flowers
# Dosage: 100 g/pump, 1 kg/acre


# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=50 , unique=True)
    product_slug = models.CharField(max_length=200, unique=True , help_text="a label for URL config" , blank=True)


    product_description = models.TextField(max_length=1000, blank=True)
    # product_price = models.IntegerField()                  
    product_image = models.ImageField(upload_to='photos/products')
    category_fk   = models.ForeignKey(Category, on_delete=models.CASCADE) #Foreign key to link with category table
    
    packaging = models.TextField(help_text="e.g. '1 kg, 25 kg'" , null=True)
    crops = models.TextField(help_text="e.g. 'Cereals, pulses, oilseeds, fruits, vegetables, flowers'",null=True)
    dosage = models.TextField(help_text="e.g. '100 g/pump, 1 kg/acre'", null=True)

    product_created_date = models.DateTimeField(auto_now_add=True)
    product_updated_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        # print("--->>>", self.Category.category_slug , self.product_slug)
        return reverse('product_details' , args=[self.category_fk.category_slug , self.product_slug])  ##to make dynamic url for each product
    
    def save(self, *args, **kwargs):
        # Automatically create slug from name if not set
        if not self.product_slug:
            # Use slugify to remove spaces/special chars, replace with '-'
            self.product_slug = slugify(self.product_name)
        super().save(*args, **kwargs)   

    def __str__(self):
        return f"{self.product_name} (Created: {self.product_created_date:%Y-%m-%d})"
