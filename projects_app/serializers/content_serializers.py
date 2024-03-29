from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from projects_app.models import Content, Gallery, GalleryImage


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'


class GalleryImagesSerializer(WritableNestedModelSerializer):

    class Meta:
        model = GalleryImage
        fields = ('file', 'order')


class GallerySerializer(WritableNestedModelSerializer):
    images = GalleryImagesSerializer(many=True)

    class Meta:
        model = Gallery
        fields = '__all__'


class ContentForProjectSerializer(WritableNestedModelSerializer):
    gallery = GallerySerializer()

    class Meta:
        model = Content
        fields = ('content_type', 'text', 'url', 'url_name', 'file', 'file_name', 'image', 'gallery')
