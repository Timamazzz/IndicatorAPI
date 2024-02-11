from rest_framework import permissions

from IndicatorAPI.utils.ModelViewSet import ModelViewSet
from projects_app.models import Project
from projects_app.serializers.project_serializers import ProjectSerializer, ProjectRetrieveSerializer, \
    ProjectListSerializer


# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_list = {
        'retrieve': ProjectRetrieveSerializer,
        'list': ProjectListSerializer,
    }
