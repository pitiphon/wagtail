"""StreamFields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndCountBlock(blocks.StructBlock):
    """Title and Text and nothing else"""

    title_and_count = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title",  blocks.CharBlock(required=True, help_text='Add your title')),
                ("icon", blocks.CharBlock(required=True, help_text='Add class icon of title', defualt="xxx")),
                ("count", blocks.TextBlock(required=True, help_text='Add count')),
            ]
        )
    )
    class Meta: # noqa
        template = "home/title_and_count_block.html"
        icon = "edit"
        label = "Title & Count"

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    subtitle = blocks.TextBlock(required=True, help_text='Add additional text')

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=True)),
            ]
        )
    )

    class Meta:  # noqa
        template = "home/card_block.html"
        icon = "placeholder"
        label = "โครงการจีโนมิกส์ไทยแลนด์"
