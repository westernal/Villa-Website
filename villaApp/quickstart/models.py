from email.policy import default
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import EmailValidator, RegexValidator, MaxValueValidator, MinValueValidator

class villa(models.Model):
    name = models.CharField(max_length = 150)
    description = models.TextField()
    price = models.CharField(max_length=50)
    image = models.ImageField(default='', upload_to='store_image/', null=True)
    created_at = models.DateTimeField(default = datetime.now)


    def __str__(self):
        return self.name



class UserManager(BaseUserManager):
        def createUser(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('Email Not Found!!!')
            user = self.model(email=self.normalize_email(email), **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

def createSuperUser(self, email, password):
        user = self.createUser(email, password)
        user.isAdmin = True
        user.isSuperUser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    userID = models.AutoField(primary_key=True)
    email= models.EmailField(max_length=100, unique=True,  validators=[EmailValidator()])
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, validators=[RegexValidator(regex="^(?=[a-z0-9._]{5,100}$)(?!.*[_.]{2})[^_.].*[^_.]$")])
    isAdmin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
