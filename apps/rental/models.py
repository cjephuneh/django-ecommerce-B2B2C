from ast import arg
from distutils.command.upload import upload
import email
from email.mime import image
from operator import mod
from statistics import mode
from tkinter import CASCADE
from turtle import title
from unicodedata import category
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=False,unique=True)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/',null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.title    

class UnitTypes(models.Model):
    name = models.CharField(max_length=150)
    unit = models.CharField(max_length=150)

    def __str__(self):
        return "{}".format(self.unit)     

    class Meta:
        verbose_name_plural = 'Unit_Types'

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    category = models.ForeignKey(
        Category, related_name='items',on_delete=models.CASCADE
    ) 
    phone = models.CharField(max_length=255,default=0)
    email = models.EmailField(max_length=20,null=True)
    slug = models.SlugField(null=False, unique=True)
    quantity = models.DecimalField(max_digits=12,default=0,decimal_places=2)
    available=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/',null=False)
    unit=models.ForeignKey(UnitTypes,related_name='unit_item',on_delete=models.CASCADE)

    def get_discounted_price(self):
        discounted_price = float( self.price - ( (self.discount*self.price) / 100 ))
        return discounted_price
    
