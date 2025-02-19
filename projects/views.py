from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    """
    API to list all projects or create a new project.
    Requires authentication.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project

@api_view(['GET'])
def project_locations(request):
    projects = Project.objects.all()
    data = [{"name": p.name, "latitude": p.latitude, "longitude": p.longitude} for p in projects]
    return Response(data)
