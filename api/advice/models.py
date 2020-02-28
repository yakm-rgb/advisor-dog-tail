from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

from api.utils.models import UUIDModel, TitleSlugModel


class Tag(UUIDModel, TitleSlugModel, TimeStampedModel):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
        indexes = (
            models.Index(fields=('title',)),
        )
        unique_together = ('title', 'slug')

class Advice(UUIDModel, TitleSlugModel, TimeStampedModel):
    """
    An advice model for storing usefull links.
    """

    link = models.URLField(_("uri link"))
    tags = models.ManyToManyField(
        Tag, 
        blank=True, 
        through='Mapping',
        verbose_name=_("advice's tags")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("advice")
        verbose_name_plural = _("advices")


class Mapping(UUIDModel, TimeStampedModel):
    """
    Mapping entry between advice and tag model instance
    """
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    advice = models.ForeignKey('Advice', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("advice's tags")
        verbose_name_plural = _("advices' tags")
        unique_together = ('tag', 'advice')
        indexes = (
            models.Index(fields=('tag','advice')),
        )