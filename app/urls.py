from django.urls import path
from .views import (
    StudentListCreateView, StudentDetailView,
    CourseListCreateView, CourseDetailView,
    YearLevelListCreateView, YearLevelDetailView
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('yearlevels/', YearLevelListCreateView.as_view(), name='yearlevel-list'),
    path('yearlevels/<int:pk>/', YearLevelDetailView.as_view(), name='yearlevel-detail'),
]