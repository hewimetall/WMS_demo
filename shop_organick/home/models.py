from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    subpage_types = ['home.Category']

    class Meta:
        verbose_name = "homepage"


class Category(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображения"
    )
    subpage_types = ['home.Product']

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
    ]
    promote_panels = []
    settings_panels = []

    class Meta:
        verbose_name = "категория"


class Product(Page):
    description = RichTextField(verbose_name="Описания",
                                features=['h2', 'h3', 'bold', 'italic', 'link', 'ol', 'ul', 'blockquote'])
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Изображения"
    )
    cost = models.FloatField(verbose_name="стоймость",
                             help_text="может быть не целой",
                             default=0.)
    count = models.PositiveSmallIntegerField(verbose_name="количество",
                                             help_text="только целое положительное значения",
                                             default=0)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('cost'),
            FieldPanel('count'),
            ImageChooserPanel('image'),
        ],
            heading="Доп имформация о товаре",
            classname="collapsible "
        ),
        FieldPanel('description', classname="full "),

    ]
    promote_panels = []
    settings_panels = []

    class Meta:
        verbose_name = "Продукт"
