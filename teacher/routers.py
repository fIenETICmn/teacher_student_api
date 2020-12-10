from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from student.api.viewset import UserViewSet, TeacherViewSet, StudentViewSet, EmployeteacherViewSet
from student.api import viewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'users', viewset.UserViewSet)
router.register(r'teachers', viewset.TeacherViewSet)
router.register(r'students', viewset.StudentViewSet)
router.register(r'employeteachers', viewset.EmployeteacherViewSet)
# router.register(r'teacher_administrators', viewset.Teacher_administratorViewSet)
# router.register(r'teacher_assistants', viewset.Teacher_assistantViewSet)
# router.register(r'teacher_regulars', viewset.Teacher_regularViewSet)

# API endpoints
urlpatterns = format_suffix_patterns([
    # path('', api_root),
    path('', include(router.urls)),
])
urlpatterns += router.urls