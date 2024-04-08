from rest_framework.fields import Field
from wagtail import blocks
from wagtail.api.v2.serializers import PageSerializer, BaseSerializer
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.rich_text import expand_db_html



class RichTextSerializableField(Field):
    def to_representation(self, value):
        return expand_db_html(value)


class ImageSerializerField(Field):
    def to_representation(self, value):
        return {
            "url": value.file.url,
            "title": value.title,
        }


class RichTextFieldBlock(blocks.RichTextBlock):
    def get_api_representation(self, value, context=None):
        return expand_db_html(str(value))


class ImageChooserBlockField(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        return {
            "url": value.file.url,
            "title": value.title,
            "width": value.width,
            "height": value.height
        }

class DocumentChooserBlockField(DocumentChooserBlock):
    def get_api_representation(self, value, context=None):
        return {
            "url": value.file.url,
            "title": value.title,
        }

