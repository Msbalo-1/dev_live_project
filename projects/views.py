from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project.html', context)

def project(request, pk):

    projectobj = Project.objects.get(id=pk)
    context = {'project': projectobj}
    return render(request, 'projects/single_project.html', context)


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project-forms.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}

    return render(request, 'projects/project-forms.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete-project.html', {'object': project})

