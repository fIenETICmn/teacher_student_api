from django import forms
from .models import User, Teacher, Student


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'username',)


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name','last_name', 'teaching_since','instrument','email','role',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name','last_name','skill_level','instrument','student_since','email',)