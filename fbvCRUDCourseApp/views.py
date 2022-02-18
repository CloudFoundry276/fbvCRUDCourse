from django.shortcuts import render, redirect
from fbvCRUDCourseApp.forms import CourseForm
from fbvCRUDCourseApp.models import Course


# Create your views here.
def getCourses(request):
    courses = Course.objects.all()
    return render(request, "fbvCRUDCourseApp/index.html", {"courses": courses})


def addCourse(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    return render(request, "fbvCRUDCourseApp/create.html", {"form": form})


def updateCourse(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "fbvCRUDCourseApp/update.html", {"form": form})


def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/")
