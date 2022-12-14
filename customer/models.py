from django.contrib.auth import get_user_model
from django.db import models
# from django.utils import timezone
from master.models import TimeStamp
from user.models import Profile

USER = get_user_model()


class Customer(TimeStamp, models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.SET_NULL,blank= True,null=True)

    user=models.OneToOneField(USER,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user}"
    


# Create your models here.
