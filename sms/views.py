from django.shortcuts import render
from .models import *


# Create your views here.

def testRecord(request):
    context = {
        'fname': "Amey",
        'lname': "Deshpande"
    }
    return render(request, "testrecords.html", context)


def addTest(request, number):
    out = ""
    for x in range(number):
        out += str(x)
    context = {
        'fname': "Amey",
        'lname': "Deshpande",
        'i': out,
        'number': number
    }
    return render(request, "addtestrecords.html", context)


def addTestMarks(request, numR):
    subject = request.POST["sub"]
    datet = request.POST["dateT"]
    tmarks = request.POST["tmarks"]
    desc = request.POST["description"]
    tea = Teacher.objects.get(id=1)
    test = Test.objects.create(subject=subject, date=datet, desc=desc, tm=tmarks, teacher=tea)
    for i in range(numR):
        sid = request.POST["studentID" + str(i)]
        om = request.POST["obtainedmarks" + str(i)]
        rmks = request.POST["remarks" + str(i)]
        stu = Student.objects.get(rno=3225)
        test2 = TestRecord.objects.create(stu=stu, marks=om, test=test, rks=rmks)
        print(test)
    context = {
        'fname': "Amey",
        'lname': "Deshpande",
        'snackBar': True,
        'snackBarStyle': 'hsdone',
        'SnackBarText': 'Test Data added Successfully'
    }
    return render(request, "testrecords.html", context)


def attendance(request):
    m = Student.objects.all()
    print(m)
    context = {
        'fname': "Amey",
        'lname': "Deshpande",
        'student': m
    }

    return render(request, "Attendance.html", context)
