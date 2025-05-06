import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class RoleCHoises(models.TextChoices):
    librarian =('librarian','Librarian')
    reader =('reader','Reader')
    admin = ('admin','Admin')
    



class User(AbstractUser):
    phone_number = models.CharField(max_length=11,null=True,blank=True)
    role = models.CharField(max_length = 100, choices = RoleCHoises, default = RoleCHoises.reader)
    email = models.EmailField(unique = True,max_length=254)




def exp_time_now():
    return timezone.now()+timedelta(minutes=2)


def generic_code():
   return random.randint(100000,999999)


class Code(models.Model):
    code = models.PositiveIntegerField(default=generic_code)
    user = models.ForeignKey(User, on_delete = models.CASCADE,related_name = 'code')
    expired_date = models.DateTimeField(default = exp_time_now)


    
    
    