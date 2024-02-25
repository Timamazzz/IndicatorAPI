from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from IndicatorAPI.utils.fields import PhoneField
from projects_app.models import Project
from projects_app.serializers.content_serializers import ContentForProjectSerializer
from django.utils.translation import gettext_lazy as _


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    views = serializers.SerializerMethodField()

    def get_views(self, obj):
        return obj.get_views_count()

    class Meta:
        model = Project
        fields = ('id', 'views', 'header_file', 'header_html', 'title', 'description', 'tags')


class ProjectRetrieveSerializer(WritableNestedModelSerializer):
    contents = ContentForProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'date', 'contents')


class ProjectDiscussFormSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, label=_("Ваше имя"), style={'column': 1})
    phone = PhoneField(required=True, label=_("Телефон"), style={'column': 2})
    email = serializers.EmailField(required=True, label=_("Электронная почта"), style={'column': 3})
    description = serializers.CharField(required=True, label=_("Описание проекта"), style={'column': 1})
    files = serializers.FileField(required=False, label=_("Файлы"), style={'column': 1})
