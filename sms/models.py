from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    rno = models.IntegerField(default=0, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


# Create your models here.
class Test(models.Model):
    subject = models.CharField(max_length=44)
    date = models.DateField()
    desc = models.CharField(max_length=85)
    tm = models.IntegerField(default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject + " " + self.desc


class TestRecord(models.Model):
    stu = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student')
    marks = models.IntegerField(default=0)
    rks = models.CharField(max_length=44)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test')

    def __str__(self):
        return str(self.stu) + " " + str(self.marks)


class Attendance(models.Model):
    date = models.DateField()
    stu = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_pre = models.BooleanField(default=False)

class Notice(models.Model):
    date = models.CharField(max_length=10)
    notice = models.CharField(max_length=300)
    def __str__(self):
        return self.date