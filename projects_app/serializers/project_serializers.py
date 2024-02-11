from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from projects_app.models import Project
from projects_app.serializers.content_serializers import ContentForProjectSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('date', )


class ProjectRetrieveSerializer(WritableNestedModelSerializer):
    contents = ContentForProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'date', 'contents')
