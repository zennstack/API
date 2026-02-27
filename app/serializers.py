from rest_framework import serializers
from .models import Student, Course, YearLevel

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'coursename', 'units']

class YearLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearLevel
        fields = ['id', 'yearlevel']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'studentname', 'age', 'course', 'yearlevel']
