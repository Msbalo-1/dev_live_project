from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import searchProject, projectPaginator
from .models import Project
from .forms import ProjectForm, reviewForm

def projects(request):
    projects, search_query = searchProject(request)
    custom_range, projects = projectPaginator(request, projects, 6)
    context = {'projects': projects, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'projects/project.html', context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    form = reviewForm()
    if request.method == 'POST':
        form = reviewForm(request.POST)
        review = form.save()
        review.project = projectobj
        review.owner = request.user.profile
        review.save()
        projectobj.getVoteCount
        messages.success(request, 'Review was Submitted  Successfully ')
        return redirect('project', pk=projectobj.id)

    context = {'project': projectobj, 'form': form}
    return render(request, 'projects/single_project.html', context)


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Project Successfully Created ')
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project-forms.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project Successfully Updated')
            return redirect('account')
    context = {'form': form}

    return render(request, 'projects/project-forms.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project Successfully Deleted')
        return redirect('account')
    return render(request, 'projects/delete-project.html', {'object': project})

