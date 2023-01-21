from django.shortcuts import render
from django.http import HttpResponse

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
    # name = 'ms balo'

    context = {'projects': projectsList}
    return render(request, 'projects/project.html', context)

def project(request, pk):

    projectobj = None
    for i in projectsList :
        if i['id'] == str(pk):
            projectobj = i
    return render(request, 'projects/single_project.html', {'project': projectobj})


