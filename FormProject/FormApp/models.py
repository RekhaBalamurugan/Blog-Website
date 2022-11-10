from django.db import models

# Create your models here.

class ModelName(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(max_length=100)
    text= models.CharField(max_length=200)
    
    

    def __str__(self):
        return self.name 
