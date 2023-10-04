import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your models here.
class UserManager(BaseUserManager):
        # get user instance with provide public_id
        def get_object_by_public_id(self, public_id):
            try:
                instance = self.get(public_id=public_id)
                return instance
            except(ObjectDoesNotExist, ValueError, TypeError):
                raise Http404
    

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
        

class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    bio = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='images/avatar', blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    
    def __str__(self) -> str:
        return f'{self.email}'
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    
    
        
    
