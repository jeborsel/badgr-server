from django.db import models
from django.conf import settings

from autoslug import AutoSlugField
import cachemodel

from credential_store.models import StoredBadgeInstance

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Collection(cachemodel.CacheModel):
    name = models.CharField(max_length=128)
    slug = AutoSlugField(
        max_length=128, populate_from='name',
        blank=False, editable=True
    )
    description = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    share_hash = models.CharField(max_length=255, null=False, blank=True)

    instances = models.ManyToManyField(
        StoredBadgeInstance, through='StoredBadgeInstanceCollection'
    )
    shared_with = models.ManyToManyField(
        AUTH_USER_MODEL, through='CollectionPermission', related_name='shared_with_me'
    )

    class Meta:
        unique_together = ('owner', 'slug')


class StoredBadgeInstanceCollection(models.Model):
    instance = models.ForeignKey(StoredBadgeInstance, null=False)
    collection = models.ForeignKey(Collection, null=False)

    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('instance', 'collection')


class CollectionPermission(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=False)
    collection = models.ForeignKey(Collection, null=False)

    can_write = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'collection')