from django.urls import path
from .views import ProjectListCreateView, project_locations

urlpatterns = [
    path('', ProjectListCreateView.as_view(), name='projects'),
    path('locations/', project_locations, name='project-locations'),

]
