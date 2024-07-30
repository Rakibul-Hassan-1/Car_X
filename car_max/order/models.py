from django.db import models
from django.contrib.auth.models import User
from car.models import Car

# Create your models here.
class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Order')
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.car}"

    