from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from penjadwalan_genetika.apps.study_programs.models import StudyPrograms
from .forms import StudyProgramForm


def index(request):
    study_programs = StudyPrograms.objects.all().order_by('-id')

    q = request.GET.get('q')
    if q:
        study_programs = study_programs.filter(name__icontains=q)

    context = {
        "study_programs": study_programs,
        "q": q
    }
    return render(request, "backoffice/study_programs/index.html", context)


def add(request):
    form = StudyProgramForm(data=request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        form.save()
        messages.success(request, "Program Studi berhasil di tambahkan")
        return redirect('backoffice:study_programs:index')

    return render(request, "add.html", context)


def detail(request, id):
    study_program = get_object_or_404(StudyPrograms, id=id)
    form = StudyProgramForm(data=request.POST or None, instance=study_program)
    if form.is_valid():
        form.save()
        messages.success(request, "Program Studi berhasil di tambahkan")
        return redirect('backoffice:study_programs:index')

    context = {
        "study_program": study_program,
        "form": form,
        "action": "Edit Program Studi"
    }

    return render(request, "backoffice/study_programs/detail.html", context)


def delete(request, id):
    study_program = get_object_or_404(StudyPrograms, id=id)
    study_program.is_active = False
    study_program.save()
    messages.success(request, "Program Studi Di Non Aktifkan")
    return redirect('backoffice:study_programs:index')


def active(request, id):
    study_program = get_object_or_404(StudyPrograms, id=id)
    study_program.is_active = True
    study_program.save()
    messages.success(request, "Program Studi Di Aktifkan")
    return redirect('backoffice:study_programs:index')
