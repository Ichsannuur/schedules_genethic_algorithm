from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from penjadwalan_genetika.apps.lecturers.models import Lecture
from .forms import LectureForm


def index(request):
    lecturers = Lecture.objects.all().order_by('-id')

    q = request.GET.get('q')
    if q:
        lecturers = lecturers.filter(name__icontains=q)

    context = {
        "lecturers": lecturers,
        "q": q
    }
    return render(request, "backoffice/lecturers/index.html", context)


def add(request):
    form = LectureForm(data=request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Dosen berhasil di tambahkan")
        return redirect('backoffice:lecturers:index')

    return render(request, "add.html", context)


def detail(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    form = LectureForm(data=request.POST or None, instance=lecture)
    if form.is_valid():
        form.save()
        messages.success(request, "Dosen berhasil di tambahkan")
        return redirect('backoffice:lecturers:index')

    context = {
        "lecture": lecture,
        "form": form,
        "action": "Edit Dosen"
    }

    return render(request, "backoffice/lecturers/detail.html", context)


def delete(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    lecture.is_active = False
    lecture.save()
    messages.success(request, "Dosen Di Non Aktifkan")
    return redirect('backoffice:lecturers:index')


def active(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    lecture.is_active = True
    lecture.save()
    messages.success(request, "Dosen Di Aktifkan")
    return redirect('backoffice:lecturers:index')
