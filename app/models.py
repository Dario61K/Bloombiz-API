from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.db import models

import uuid

class UserManager(BaseUserManager):
    
    def create_user(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(password, **extra_fields)
    

class User(AbstractBaseUser):
    id = models.UUIDField('id', primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField('full_name', max_length=150)
    email = models.EmailField('email', unique=True)
    is_superuser = models.BooleanField('is super user', default=False)
    created_at = models.DateTimeField('created at', default=timezone.now)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.full_name}"
    
