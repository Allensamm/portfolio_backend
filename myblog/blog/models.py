# models.py
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from tinymce.models import HTMLField

class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = AppUserManager()

    @property
    def custom_identifier(self):
        # Use a combination of fields that uniquely identify the user
        return f"{self.email}-{self.username}"

    @property
    def id(self):
        return self.pk

class Post(models.Model):
    
    CATEGORY_CHOICES = [
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('javascript', 'JavaScript'),
        # Add more categories as needed
    ]
    
    projectname = models.CharField(max_length=255)
    Description = models.TextField()
    anyfile = models.FileField(upload_to='files/', null=True, blank=True)
    linktoproject = models.URLField(null=True)
    largecontent = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    category = models.CharField(max_length = 20, choices=CATEGORY_CHOICES,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.projectname
