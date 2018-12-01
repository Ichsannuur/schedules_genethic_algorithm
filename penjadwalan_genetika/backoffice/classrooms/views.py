from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from penjadwalan_genetika.apps.classrooms.models import Classroom
from .forms import ClassroomForm


def index(request):
    classrooms = Classroom.objects.all().order_by('-id')

    q = request.GET.get('q')
    if q:
        classrooms = classrooms.filter(name__icontains=q)

    context = {
        "classrooms": classrooms,
        "q": q
    }
    return render(request, "backoffice/classrooms/index.html", context)


def add(request):
    form = ClassroomForm(data=request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Ruangan berhasil di tambahkan")
        return redirect('backoffice:classrooms:index')

    return render(request, "add.html", context)


def detail(request, id):
    classroom = get_object_or_404(Classroom, id=id)
    form = ClassroomForm(data=request.POST or None, instance=classroom)
    if form.is_valid():
        form.save()
        messages.success(request, "Ruangan berhasil di tambahkan")
        return redirect('backoffice:classrooms:index')

    context = {
        "classroom": classroom,
        "form": form,
        "action": "Edit Ruangan"
    }

    return render(request, "backoffice/classrooms/detail.html", context)


def delete(request, id):
    classroom = get_object_or_404(Classroom, id=id)
    classroom.is_active = False
    classroom.save()
    messages.success(request, "Ruangan Di Non Aktifkan")
    return redirect('backoffice:classrooms:index')


def active(request, id):
    classroom = get_object_or_404(Classroom, id=id)
    classroom.is_active = True
    classroom.save()
    messages.success(request, "Ruangan Di Aktifkan")
    return redirect('backoffice:classrooms:index')
