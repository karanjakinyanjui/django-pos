# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class DeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=True)


class NotDeletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class AbstractBaseModel(models.Model):
    deleted = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True,
                                   null=True, blank=True, )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updated",
        related_query_name="%(app_label)s_%(class)s_updated"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created",
        related_query_name="%(app_label)s_%(class)s_created"
    )

    class Meta:
        abstract = True

    objects = NotDeletedManager()
    all_objects = models.Manager()
    deleted_objects = DeletedManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()
