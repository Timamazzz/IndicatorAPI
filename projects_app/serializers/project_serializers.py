from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from IndicatorAPI.utils.fields import PhoneField
from projects_app.models import Project
from projects_app.serializers.content_serializers import ContentForProjectSerializer


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
        exclude = ('date',)


class ProjectRetrieveSerializer(WritableNestedModelSerializer):
    contents = ContentForProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'date', 'contents')


class ProjectDiscussFormSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, label="Ваше имя", style={'column': 1})
    phone = PhoneField(required=True, label="Телефон", style={'column': 2})
    email = serializers.EmailField(required=True, label="Электронная почта", style={'column': 3})
    description = serializers.CharField(required=True, label="Описание проекта", style={'column': 1})
    files = serializers.FileField(required=False, label="Файлы", style={'column': 1})
