from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from core.models import TimeStampedModel
from .managers import PublishedServiceQuerySet


class Service(TimeStampedModel):
    """An IT service offering shown on the site.

    Inherits ``created_at`` / ``updated_at`` from the shared core base so the
    module stays consistent with the rest of the project.
    """

    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    # Bootstrap icon class, e.g. "bi-cloud-fill" (icons are already bundled).
    icon = models.CharField(
        max_length=60,
        default='bi-gear-fill',
        help_text='Bootstrap icon class, e.g. "bi-cloud-fill".',
    )

    summary = models.CharField(max_length=255, help_text='Short one-line summary shown in cards.')
    description = models.TextField(blank=True, help_text='Full description shown on the service detail page.')

    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=True, help_text='Show this service on the home page.')
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers are shown first.')

    objects = PublishedServiceQuerySet.as_manager()

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug})
