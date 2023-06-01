from django.contrib import admin
from .models import Category,Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    List_display = ['name','slug']
    Prepopulated_fields ={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)




class ProductAdmin(admin.ModelAdmin):
    List_display = ['name','price','stock','available','created','updated']
    List_editable = ['price','stock','available']
    Prepopulated_fields ={'slug':('name',)}
    List_per_page = 20
admin.site.register(Product,ProductAdmin)


from django.db import models

# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product',blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)