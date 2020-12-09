from student.models import User, Teacher, Student, Employeteacher
from student.api.serializers import UserSerializer, TeacherSerializer, StudentSerializer, EmployeteacherSerializer
from rest_framework import viewsets
from rest_framework import permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.DjangoModelPermissions]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EmployeteacherViewSet(viewsets.ModelViewSet):
    queryset = Employeteacher.objects.all()
    serializer_class = Employeteacher


# class Teacher_administratorViewSet(viewsets.ModelViewSet):
#     queryset = Teacher.objects.filter(role='administrator')
#     serializer_class = TeacherSerializer
#     # permission_classes = [permissions.DjangoModelPermissions]
#
#
# class Teacher_assistantViewSet(viewsets.ModelViewSet):
#     queryset = Teacher.objects.filter(role='assistant')
#     serializer_class = TeacherSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#
# class Teacher_regularViewSet(viewsets.ModelViewSet):
#     queryset = Teacher.objects.filter(role='regular_teacher')
#     serializer_class = TeacherSerializer
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]