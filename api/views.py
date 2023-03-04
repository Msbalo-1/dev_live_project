from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import projectSerializers
from projects.models import Project, Review

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
@permission_classes([IsAuthenticated])
def getProjects(request):
    print('USER:', request.user)
    projects = Project.objects.all()
    serializer = projectSerializers(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request, pk=id):
    project = Project.objects.get(id=pk)
    serializer = projectSerializers(project, many=False)
    return Response(serializer.data)


@api_view(['POST', 'PUT'])
def projectVote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
    )
    review.value = data['value']
    review.save()
    project.getVoteCount

    serializer = projectSerializers(project, many=False)
    return Response(serializer.data)




