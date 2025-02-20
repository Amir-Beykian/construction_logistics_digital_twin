from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_project(request):
    """Allows project users to register their projects."""
    if request.user.role != "project":
        return Response({"error": "Unauthorized"}, status=403)

    data = request.data
    project = Project.objects.create(
        owner=request.user,
        name=data["name"],
        location=data["location"],
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
    )

    return Response({"message": "Project created successfully", "project_id": project.id})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_projects(request):
    """Returns all projects owned by the authenticated project user."""
    if request.user.role != "project":
        return Response({"error": "Unauthorized"}, status=403)

    projects = Project.objects.filter(owner=request.user)
    return Response([
        {"id": p.id, "name": p.name, "location": p.location, "latitude": p.latitude, "longitude": p.longitude}
        for p in projects
    ])


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, project_id):
    """Allows project users to delete their projects."""
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    project.delete()
    return Response({"message": "Project deleted successfully"})