from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class districtTable(models.Model):
    district_name = models.CharField(max_length = 45,unique=True)
    short_code = models.CharField(max_length=5, unique=True)
    Country = models.CharField(max_length=255,choices=(
        ('India','India'),
        ('Australia','Australia'),
    ))
    Zone = models.CharField(max_length=255,choices=(
        ('South zone','South zone'),
        ('North zone','North zone'),
    ))
    Sub_zone = models.CharField(max_length=100,choices=(
        ('Kerala','Kerala'),
        ('Tamilnadu','Tamilnadu'),
    ))
    status = models.Model(max_length=10,choices=(
        ('Active','Active'),
        ('inactive','inactive'),
        ('Suspended','Suspended'),
    ))
    Created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'districtTable'
    def __str__(self):
        return self.district_name

class AreaTable(models.Model):
    Area_name = models.CharField(max_length=255)
    Short_code = models.CharField(max_length=5, unique=True)
    Country = models.CharField(max_length=255,choices=(
        ('India','India'),
        ('Australia','Australia'),
    ))
    Zone = models.CharField(max_length=255,choices=(
        ('South zone','South zone'),
        ('North zone','North zone'),
    ))
    Sub_zone = models.CharField(max_length=100,choices=(
        ('Kerala','Kerala'),
        ('Tamilnadu','Tamilnadu'),
    ))
    District = models.ForeignKey(districtTable, on_delete=models.CASCADE)
    status = models.Model(max_length=10,choices=(
        ('Active','Active'),
        ('inactive','inactive'),
        ('Suspended','Suspended'),
    ))
    Created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'area_table'
    def __str__(self):
        return self.Area_name

class RegionTable(models.Model):
    Region_name = models.CharField(max_length=255)
    Short_code = models.CharField(max_length=5,unique=True)
    Country = models.CharField(max_length=255,choices=(
        ('India','India'),
        ('Australia','Australia'),
    ))
    Zone = models.CharField(max_length=255,choices=(
        ('South zone','South zone'),
        ('North zone','North zone'),
    ))
    Sub_zone = models.CharField(max_length=100,choices=(
        ('Kerala','Kerala'),
        ('Tamilnadu','Tamilnadu'),
    ))
    Diviosion = models.ForeignKey(districtTable, on_delete=models.CASCADE)
    Area = models.ForeignKey(AreaTable, on_delete=models.CASCADE)
    Region_message = models.TextField()
    Status = models.CharField(max_length=20, choices=(
        ('Active','Active'),
        ('Inactive','Inactive'),
        ('Suspended','Suspended'),
    ))
    Created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'region_table'
    def __str__(self):
        return self.Region_name

