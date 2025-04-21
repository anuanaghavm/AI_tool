from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, phone_number, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone_number=phone_number, **extra_fields)
        # Store password directly without hashing
        user.password = password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, phone_number, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=128)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone_number']

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        # Store password directly without hashing
        self.password = raw_password

    def check_password(self, raw_password):
        # Compare passwords directly
        return self.password == raw_password
