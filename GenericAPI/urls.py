from django import views
from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StudentCreate.as_view()),
    path('stulist/', views.StudentList.as_view()),
    path('sturetrive/<int:pk>/', views.StudentRetrive.as_view()),
    path('stuupdate/<int:pk>/', views.StudentUpdate.as_view()),
    path('studelete/<int:pk>/', views.StudentDelete.as_view()),
]
