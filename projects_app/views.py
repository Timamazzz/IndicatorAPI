from django.core.files.base import ContentFile
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
from django.utils.translation import gettext_lazy as _


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
            files = request.FILES
            print('files', files)
            print('request', request.__dict__)
            send_files = {}
            for file in files:
                send_files[file.name] = ContentFile(file.read(), name=file.name)

            subject = _("Новое обсуждение проекта")
            message = _("Имя: {name}\nТелефон: {phone}\nЭлектронная почта: {email}\nОписание: {description}").format(
                name=name, phone=phone, email=email, description=description
            )
            html_message = _(
                "<p><strong>Имя:</strong> {name}</p><p><strong>Телефон:</strong> {phone}</p><p><strong>Электронная почта:</strong> {email}</p><p><strong>Описание:</strong> {description}</p>").format(
                name=name, phone=phone, email=email, description=description
            )

            mail.send(
                'timforworking@mail.ru',
                settings.DEFAULT_FROM_EMAIL,
                subject=subject,
                message=message,
                html_message=html_message,
                priority='now',
                attachments=send_files
            )
            return Response({"success": True}, status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
