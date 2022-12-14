from datetime import datetime, timedelta
from statistics import mode

import jwt
from django.contrib.auth.hashers import (check_password, is_password_usable,
                                         make_password)
from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager)
from django.db import models

# # Create your models here.
# class MyUserMenager(BaseUserManager):
#     def create_user(self,username, email, password, **extra_fields):
#         user=self.model(
#             email=email,
#             username=username,
#             password=password
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, username, email,  password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#         extra_fields.setdefault('is_admin', True)

#         if extra_fields.get('is_staff') is not True:    
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):

    MEMBER_POSITION = (
        ('Chairman', 'Chairman'),
        ('Menager', 'Menager'),
        ('Worker', 'Worker')
    )
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=250)
    birth_date = models.DateField(null=True, blank=True)
    member_position = models.CharField(max_length=20, choices=MEMBER_POSITION)

    # objects = MyUserMenager()   
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        permissions = (
            ("worker_permission", "Worker permissions"),
            ("menager_permission", "Menager permissions"),
            ("chairman_permission", "Chairman ermissions")
        )

    # @property
    # def token(self):
    #     token = jwt.encode(
    #         {
    #             'username': self.username,
    #             'email': self.email,
    #             'exp': datetime.utcnow() + timedelta(hours=24)
    #         }, 'key', algorithm='HS256'
    #     )

