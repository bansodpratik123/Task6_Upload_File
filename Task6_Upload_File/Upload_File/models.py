from django.db import models

# Create your models here.
class Cities(models.Model):
    City_Name=models.CharField(max_length=50)
    Image=models.FileField(upload_to='images/')