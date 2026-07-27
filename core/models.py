from django.db import models


class TimeStampedModel(models.Model):
    """Abstract base model that new modules can inherit from.

    Provides self-managing ``created_at`` / ``updated_at`` timestamps so every
    module shares the same auditing fields without re-implementing them.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class PublishableModel(TimeStampedModel):
    """Abstract base for content that can be shown or hidden on the site.

    Combined with :class:`TimeStampedModel` this gives new content modules a
    consistent publish workflow and ordering out of the box.
    """

    is_published = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text='Lower numbers are shown first.')

    class Meta:
        abstract = True
        ordering = ['order', '-created_at']
