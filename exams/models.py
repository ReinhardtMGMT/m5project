from django.db import models
import uuid

# Create your models here.


class Exams(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    score = models.CharField()
    user = models.ForeignKey('custom_user.User', related_name='exams')
