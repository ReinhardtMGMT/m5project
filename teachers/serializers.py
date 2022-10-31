from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name","age","address","contacts","email","password","is_teacher","cpf","rg"]
        extra_kwargs = {'password': {'required': True,'write_only': True}}
        depth = 1

    def create(self, email, cpf, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        Teacher.objects.create(user=user, cpf=cpf)
        return user