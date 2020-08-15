# Generated by Django 3.0.7 on 2020-06-24 11:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200624_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField([('cards', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('subtitle', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.core.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.core.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=True))])))])), ('title_and_count', wagtail.core.blocks.StructBlock([('title_and_count', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('icon', wagtail.core.blocks.CharBlock(defualt='xxx', help_text='Add class icon of title', required=True)), ('count', wagtail.core.blocks.TextBlock(help_text='Add count', required=True))])))]))], blank=True, null=True),
        ),
    ]
