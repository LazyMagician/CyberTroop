from django.db import models
from django.forms import PasswordInput

# Create your models here.
class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    thumb = models.FileField(upload_to="thumb/%y",blank=True)
    def __str__(self):
        return self.caption

# class Signup(models.Model):
#     name = models.CharField(max_length=122)
#     email = models.CharField(max_length=122)
#     password =  models.CharField(max_length=122)
  
#     def __str__(self) -> str:
#         return self.email

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone =  models.CharField(max_length=122)
    desc =  models.TextField()
    date = models.DateField()
    
    def __str__(self) -> str:
        return self.name