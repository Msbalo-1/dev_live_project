from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import projectSerializers
from projects.models import Project

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},
        {'POST': '/api/projects/id/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = projectSerializers(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk=id):
    project = Project.objects.get(id=pk)
    serializer = projectSerializers(project, many=False)
    return Response(serializer.data)

