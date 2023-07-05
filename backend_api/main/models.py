from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)

 # Product Category
class ProductCategory(models.Model):
    title models.CharField(max_length=200) 
    detail-models.TextField(null=True)

    def _str_(self):
        return self.title
# Product
class Product(models.Model):
    title models.CharField(max_length=200)
    detail models.TextField(null=True) I
    price models. FloatField()

    def _str_(self): 
        return self.title