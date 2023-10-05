import uuid
from django.db import models
from core.abstract.model import AbstractManager, AbstractModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager, AbstractManager):
        

        def create_user(self, username, email, password=None, **kwargs):
            """ Create and return user with username, email and password """
            if username is None:
                raise TypeError("User must have username")
            if email is None:
                raise TypeError("User must have email")
            if password is None:
                raise TypeError("User must have password")
            
            # create user instance wih providig username, email and additional keyword arguments
            user = self.model(username=username, email=self.normalize_email(email), **kwargs)
            # set password with hashing to it
            user.set_password(password)
            # save user instance in database
            user.save(using=self._db)
            
            return user
            
            
        def create_superuser(self, username, email, password, **kwargs):
            """ Create and return user with username, email and password """
            if username is None:
                raise TypeError("User must have username")
            if email is None:
                raise TypeError("User must have email")
            if password is None:
                raise TypeError("User must have password")
            
            user = self.create_user(username, email, password, **kwargs)
            user.is_superuser = True
            user.is_staff = True
            user.save(using=self._db)
            
            return user
        

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    bio = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='images/avatar', blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
  
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    
    def __str__(self) -> str:
        return f'{self.email}'
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
        
    
