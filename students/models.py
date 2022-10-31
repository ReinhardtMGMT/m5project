from django.db import models

from utils.base_user import CustomUser
# Create your models here.
# class Student(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
#     name=models.TextField()
#     age= models.IntegerField()
#     contacts= models.TextField()
#     email=models.EmailField()
#     password= models.TextField()
#     rg=models.TextField()
#     is_teacher= models.BooleanField()

#     address = models.OneToOneField("addresses.Address", related_name="user")

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)