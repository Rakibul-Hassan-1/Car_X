from django.db import models
from brand.models import Brand

# Create your models here.
class Car(models.Model):
    model_name=models.CharField(max_length=100)
    brand_name=models.ForeignKey(Brand,on_delete=models.CASCADE)
    description=models.TextField()
    price = models.IntegerField()
    quantity= models.IntegerField()
    image=models.ImageField(upload_to="car/media/uploads/")

    def __str__(self):
        return f"{self.model_name}- {self.brand_name}"


class Comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="comments", blank=True,null=True)  
    name= models.CharField(max_length=80)
    email= models.EmailField()
    body=models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return f"Comments by {self.name}"      