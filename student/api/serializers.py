from rest_framework import serializers
from student.models import User, Teacher, Student, Employeteacher


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'id', 'url',)


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'teaching_since', 'instrument', 'email', 'role', 'id', 'url',)


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'skill_level', 'instrument', 'student_since', 'email', 'birth_date', 'id', 'url',)


class EmployeteacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employeteacher
        fields = ('name_school', 'address', 'phone_no', 'id', 'url',)