from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/project.html', context)

def project(request, pk):

    projectobj = Project.objects.get(id=pk)
    # tags = projectobj.tags.all()
    # reviews = projectobj.review_set.all()
    context = {'project': projectobj}


    return render(request, 'projects/single_project.html', context)


