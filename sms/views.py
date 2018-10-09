from django.shortcuts import render
import datetime
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
    if request.method == "GET":
        m = Student.objects.all()
        print(m)
        context = {
            'fname': "Amey",
            'lname': "Deshpande",
            'student': m
        }
        return render(request, "Attendance.html", context)
    else:
        m = Student.objects.all()
        dateT = request.POST["dateT"]
        for i in m:
            ap = request.POST.get("ap" + str(i.rno))
            if not ap:
                attend = Attendance.objects.create(date=dateT, stu=i)
        context = {
            'fname': "Amey",
            'lname': "Deshpande",
            'snackBar': True,
            'snackBarStyle': 'hsdone',
            'SnackBarText': 'Test Data added Successfully'
        }
        return render(request, "testrecords.html", context)
def aft(request):
    if request.method == "GET":
        context = {
            'fname': "Amey",
            'lname': "Deshpande",
        }
        return render(request, "aft.html", context)
    else:
        subject = request.POST["sub"]
        datet = request.POST["dateT"]
        tmarks = request.POST["tmarks"]
        desc = request.POST["description"]
        tea = Teacher.objects.get(id=1)
        test = Test.objects.create(subject=subject, date=datet, desc=desc, tm=tmarks, teacher=tea)
        context = {
            'fname': "Amey",
            'lname': "Deshpande",
            'snackBar': True,
            'snackBarStyle': 'hsdone',
            'SnackBarText': 'New Test Data added Successfully'
        }
        return render(request, "testrecords.html", context)


def aftList(request):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=6)
    test = Test.objects.all()
    context = {
        'fname': "Amey",
        'lname': "Deshpande",
        'test': test
    }
    return render(request, "testlist.html", context)

def login1(request):

    return 0

def absent(request):
        pass
#     arecords = Absent.objects.filter(sid=1)
#
#     return render(request, 'absent.html', {'records': arecords})

def notice(request):

    arecords = Notice.objects.all()

    return render(request, 'notice.html', {'records': arecords})

def profile(request):

    return render(request, 'profilestudent.html', {})

def profilep(request):

    return render(request, 'parentprofile.html', {})