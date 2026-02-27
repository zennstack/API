from django.db import models

class Course(models.Model):
    coursename = models.CharField(max_length=200)
    units = models.IntegerField()

    def __str__(self):
        return self.coursename

class YearLevel(models.Model):
    yearlevel = models.CharField(max_length=50)

    def __str__(self):
        return self.yearlevel

class Student(models.Model):
    studentname = models.CharField(max_length=200)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    yearlevel = models.ForeignKey(YearLevel, on_delete=models.SET_NULL, null=true)
    
    def __str__(self):
        return self.studentname

