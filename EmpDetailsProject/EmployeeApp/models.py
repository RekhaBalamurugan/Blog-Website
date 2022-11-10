from django.db import models

# Create your models here.

class Users(models.Model):
    firstname=models.CharField(max_length=200,unique=True)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.firstname
