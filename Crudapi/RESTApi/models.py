from django.db import models

# Create your models here.

class Employees(models.Model):
    EmpId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    emailID = models.EmailField(blank=True,null=True)
    contactNo = models.CharField(max_length=12,blank=True,null=True)
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=64)
    product_quantity = models.IntegerField()
    product_prize = models.CharField(max_length=64)

    def __str__(self):
        return self.product_name