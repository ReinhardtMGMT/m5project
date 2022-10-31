from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["name","age","address","contacts","email","password","rg","is_teacher"]
        extra_kwargs = {'password': {'required': True,'write_only': True}}
        depth = 1

    def create(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        Student.objects.create(user=user)
        return user