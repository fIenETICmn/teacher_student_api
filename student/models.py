from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    STATUS_CHOICES = [
        ('Administrator', 'administrator'),
        ('Assistant', 'assistant'),
        ('Regular_teacher', 'regular_teacher'),
        ('Student', 'student'),
    ]
    id = models.AutoField(primary_key=True)
    role = models.CharField(choices=STATUS_CHOICES, max_length=20, null=True, default='')
    username = models.CharField(max_length=30, unique=False)
    first_name = models.CharField(null=True, max_length=200)
    last_name = models.CharField(null=True, max_length=200)
    instrument = models.CharField(null=True, max_length=100)
    email = models.EmailField(null=False, unique=True)
    skill_level = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
    student_since = models.DateField(null=True)
    teaching_since = models.DateField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Teacher(models.Model):
    STATUS_CHOICES = [
        ('Administrator', 'administrator'),
        ('Assistant', 'assistant'),
        ('Regular_teacher', 'regular_teacher'),
    ]
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False, max_length=200)
    last_name = models.CharField(null=True, max_length=200)
    teaching_since = models.DateField(null=False)
    instrument = models.CharField(null=False, max_length=100)
    email = models.EmailField(null=False, unique=True)
    role = models.CharField(choices=STATUS_CHOICES, max_length=20,null=False, default='')

    def __str__(self):
        return self.first_name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False, max_length=200)
    last_name = models.CharField(null=True, max_length=200)
    skill_level = models.IntegerField()
    instrument = models.CharField(null=False, max_length=100)
    student_since = models.DateField(null=False)
    email = models.EmailField(null=False, unique=True)
    birth_date = models.DateField(null=False)

    def __str__(self):
        return self.first_name


class Employeteacher(models.Model):
    id = models.AutoField(primary_key=True)
    name_school = models.CharField(null=False, max_length=300)
    address = models.CharField(null=False, max_length=500)
    phone_no = models.IntegerField(null=False)

    def __str__(self):
        return self.name_school

