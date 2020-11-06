from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True,upload_to='images') 
    BedNum = models.IntegerField(default='1')
    HallNum = models.IntegerField(default='1')
    kitchenNum = models.IntegerField(default='1')
    Location = models.CharField(default=' ',max_length=50)
    
    Contactno = models.IntegerField(default='0')
    RentCost = models.IntegerField(default='0')
    #Facility = models.CharField(blank=True,max_length=200)
   
    
 