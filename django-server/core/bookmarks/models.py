from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Tag(models.Model):
    name = models.CharField(unique=True, max_length=255)

class Url(models.Model):
    url_path = models.URLField(unique=True)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must provide email')

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.activated=True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
         Creates and saves a superuser with the given email and password.
        """

        USERNAME_FIELD = 'email'

        user = self.create_user(email, password=password)
        user.is_admin = True
        user.activated=True
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        """
         Creates and saves a staffuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.activated=True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    title = models.CharField(max_length=250)
    url = models.ManyToManyField(Url)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    users = models.ManyToManyField(User)


