from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
import uuid

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    
    # def create_student(self, email, password=None, **extra_fields):
    #     user = self.create_user(email, password, **extra_fields)
    #     Student.objects.create(user=user)
    #     return user
    
    # def create_teacher(self, email, cpf, password=None, **extra_fields):
    #     user = self.create_user(email, password, **extra_fields)
    #     Teacher.objects.create(user=user, cpf=cpf)
    #     return user

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email',
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name=models.TextField()
    age= models.IntegerField()
    contacts= models.TextField()
    email=models.EmailField()
    password= models.TextField()
    rg=models.TextField()
    is_teacher= models.BooleanField()

    address = models.OneToOneField("addresses.Address", on_delete=models.CASCADE, related_name="user")