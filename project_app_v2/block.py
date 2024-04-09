
from wagtail import blocks
from wagtail.blocks import CharBlock, URLBlock


class LinkBlock(blocks.StructBlock):
    name = CharBlock(required=True, help_text="Текст ссылки", max_length=128)
    link = URLBlock(required=True, help_text="url")

    class Meta:
        verbose_name = 'Описание ссылки'