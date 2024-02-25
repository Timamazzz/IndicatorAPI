from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from IndicatorAPI import settings
from IndicatorAPI.utils.ModelViewSet import ModelViewSet
from IndicatorAPI.utils.OptionsMetadata import OptionsMetadata
from projects_app.models import Project, UniqueProjectView
from projects_app.serializers.project_serializers import ProjectSerializer, ProjectRetrieveSerializer, \
    ProjectListSerializer, ProjectDiscussFormSerializer
from post_office import mail


# Create your views here.
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_list = {
        'retrieve': ProjectRetrieveSerializer,
        'list': ProjectListSerializer,
    }

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        ip_address = self.request.META.get('REMOTE_ADDR')
        user_agent = self.request.META.get('HTTP_USER_AGENT')

        UniqueProjectView.objects.get_or_create(
            project=instance,
            ip_address=ip_address,
            user_agent=user_agent
        )

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProjectDiscussAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_list = {
        'discuss': ProjectDiscussFormSerializer,
    }
    metadata_class = OptionsMetadata

    def post(self, request, *args, **kwargs):
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

