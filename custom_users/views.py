from rest_framework.views import APIView, Request, Response, status
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from .permissions import StudentIsAdminPermission
from custom_users.serializers import (
    StudentSerializer,
    TeacherSerializer,
    ListStudentSerializer,
    ListTeacherSerializer,
    UpdateStudentSerializer,
    UpdateTeacherSerializer,
)
from custom_users.models import Student, Teacher
from exams.models import Exams
from django.shortcuts import get_object_or_404
from report_cards.serializers import ListReportCardSerializer
from exams.serializers import ExamsSerializer
import ipdb

## ---------------------- Student Views ----------------------
class StudentCreateView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = StudentSerializer


class StudentsListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = ListStudentSerializer


class DeleteRetriveStudentView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_url_kwarg = "id"


class UpdateStudentView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = UpdateStudentSerializer
    lookup_url_kwarg = "id"


class GetStudentReports(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [StudentIsAdminPermission]

    def get(self, request: Request, student_id: str) -> Response:
        student = get_object_or_404(Student, id=student_id)
        self.check_object_permissions(request=request, obj=student.id)
        reports = student.report_cards
        serializer = ListReportCardSerializer(reports, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
        
class GetStudentExams(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [StudentIsAdminPermission]

    def get(self, request: Request, student_id: str) -> Response:
        student = get_object_or_404(Student, id=student_id)
        self.check_object_permissions(request=request, obj= student.id)
        exams = student.exams
        serializer = ExamsSerializer(exams, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


## ------------------------- Teacher Views --------------------------:


class TeacherCreateView(generics.CreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    serializer_class = TeacherSerializer


class TeacherListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = ListTeacherSerializer


class DeleteRetriveTeacherView(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_url_kwarg = "id"


class UpdateTeacherView(generics.UpdateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAdminUser]

    queryset = Teacher.objects.all()
    serializer_class = UpdateTeacherSerializer
    lookup_url_kwarg = "id"



