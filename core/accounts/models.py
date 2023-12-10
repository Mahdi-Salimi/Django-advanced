from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager):
    '''
    Custom User Manager for our app that extends BaseUserManager
    '''
    def create_user(self, email, password, **extra_fields):
        '''
        create and save user with given email and password and extra fields
        '''
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields)
        user.set_password(password) # set password for the user that its email setss
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        '''
        create and save superuser with given email and password and extra fields
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields) # it will return it to the main function above
                                                                #  that create user with these changes
        
    
    
class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom User Model for our app
    '''
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email