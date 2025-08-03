from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"


class UserProfile(models.Model):
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookshelf_profile')
   role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('staff', 'Staff'), ('user', 'User')])


#custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        permissions = [
            ("can_create", "Can create content"),
            ("can_delete", "Can delete content"),
        ]


