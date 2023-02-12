from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("user must have an email")
        if not password:
            raise ValueError(("please enter the password"))
        
        user = self.model(email=self.normalize_email(
        email), username=username, password=password)
        user.set_password(password)
        user.is_admin=False
        user.is_staff==False
        user.is_superuser=False

        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None):
        if not email:
            raise ValueError("user must have an email")
        if not password:
            raise ValueError(("please enter the password"))

        user = self.create_user(email=self.normalize_email(
        email), username=username, password=password)
        user.set_password(password)
        user.is_admin=True
        user.is_staff==True
        user.is_superuser=True
        user.save(using=self._db)
        return user
        
    


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    is_ambassador=models.BooleanField(default=True)
    username=models.CharField(max_length=30,unique=True)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects=UserManager()
    
