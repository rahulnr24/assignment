from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="employee/")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)

    first_address = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    country = models.CharField(max_length=122)
    pincode = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    