from django.urls import path
from . import views
from .views import signup, post_list

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('post_list/', views.post_list, name='post_list'),
]