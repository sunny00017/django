from django.db import models
<<<<<<< HEAD
from django.urls import reverse
=======
>>>>>>> main

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta: 
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
<<<<<<< HEAD
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
=======
>>>>>>> main
    
    def __str__(self):
        return self.category_name