from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtail.core.fields import StreamField
from streams import blocks


# create Oderable 
class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [ImageChooserPanel("carousel_image")]
    
# create content in home page
class HomePage(Page):
    template = "home/home_page.html"

    title_head_page = models.CharField(max_length=100, blank=False, null=True)
    name_page = models.CharField(max_length=100, blank=False, null=True, help_text="Add your name page ")
    URL_page = models.URLField(max_length = 200, blank=False, null=True, help_text="Add your URL page ")


    # @todo add streamfields
    content = StreamField(
        [
            ("cards", blocks.CardBlock()),
            ("title_and_count", blocks.TitleAndCountBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                InlinePanel("carousel_images", max_num=5, min_num=1, label="Image")
            ],
            heading="Carousel Images",
        ),
        StreamFieldPanel("content"),
        MultiFieldPanel(
            [
                FieldPanel("title_head_page"),
                FieldPanel("name_page"),
                FieldPanel("URL_page"),
            ],
            heading="page Options",
        ),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

