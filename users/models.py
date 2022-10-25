from statistics import mode
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, AbstractUser
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)


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
  
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=250)
    birth_date = models.DateField(null=True, blank=True)
    member_position = models.CharField(max_length=20, choices=MEMBER_POSITION)

    # objects = MyUserMenager()   
    REQUIRED_FIELDS = ['email']
    # USERNAME_FIELD = 'username'

    class Meta:
        permissions = (
            ("worker_permission", "Worker permissions"),
            ("menager_permission", "Menager permissions"),
            ("chairman_permission", "Chairman ermissions")
        )



