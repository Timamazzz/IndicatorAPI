from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from IndicatorAPI import settings
from IndicatorAPI.utils.ModelViewSet import ModelViewSet
from projects_app.models import Project
from projects_app.serializers.project_serializers import ProjectSerializer, ProjectRetrieveSerializer, \
    ProjectListSerializer, ProjectDiscussFormSerializer
from post_office import mail


# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_list = {
        'retrieve': ProjectRetrieveSerializer,
        'list': ProjectListSerializer,
        'discuss': ProjectDiscussFormSerializer,
    }

    @action(detail=True, methods=['post'])
    def discuss(self, request):
        serializer = ProjectDiscussFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            phone = serializer.validated_data.get('phone')
            email = serializer.validated_data.get('email')
            description = serializer.validated_data.get('description')

            subject = "New Project Discussion"
            message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nDescription: {description}"
            html_message = f"<p><strong>Name:</strong> {name}</p><p><strong>Phone:</strong> {phone}</p><p><strong>Email:</strong> {email}</p><p><strong>Description:</strong> {description}</p>"
            mail.send(
                '89205731783@mail.ru',
                settings.DEFAULT_FROM_EMAIL,
                subject=subject,
                message=message,
                html_message=html_message,
                priority='now'
            )
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
