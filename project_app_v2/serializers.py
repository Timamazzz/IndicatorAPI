from rest_framework import serializers
from wagtail.api.v2.serializers import PageSerializer


class ProjectViewPageSerializer(PageSerializer):
    views = serializers.SerializerMethodField(method_name="get_views", read_only=True)

    def get_views(self, instance):
        return instance.get_views()
