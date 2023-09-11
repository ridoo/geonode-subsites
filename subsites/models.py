import logging
import operator
from functools import reduce

from django.db import models
from django.db.models import Q
from geonode.base.models import (GroupProfile, HierarchicalKeyword, Region,
                                 TopicCategory)
from geonode.themes.models import GeoNodeThemeCustomization

logger = logging.getLogger(__name__)

class SubSite(models.Model):
    RESOURCE_TYPE = (
        ("document", "document"),
        ("map", "map"),
        ("dataset", "dataset"),
        ("dashboard", "dashboard"),
        ("geoapp", "geoapp"),
        ("geostory", "geostory"),
    )

    slug = models.SlugField(
        verbose_name="Site name",
        max_length=250,
        null=False,
        blank=False,
        unique=True,
        help_text="Sub site name, formatted as slug. This slug is going to be used as path for access the subsite",
    )
    theme = models.ForeignKey(
        GeoNodeThemeCustomization, on_delete=models.SET_NULL, null=True, default=None
    )

    region = models.ManyToManyField(Region, null=True, blank=True, default=None)
    category = models.ManyToManyField(
        TopicCategory, null=True, blank=True, default=None
    )
    keyword = models.ManyToManyField(
        HierarchicalKeyword, null=True, blank=True, default=None
    )
    groups = models.ManyToManyField(GroupProfile, null=True, blank=True, default=None)

    resource_type = models.CharField(
        null=True, blank=True, default=None, choices=RESOURCE_TYPE, max_length=100
    )

    def __str__(self) -> str:
        return self.slug

    def filter_by_subsite_condition(self, qr):
        """
        Filter any input input resource queryset (resources, doc, map, dataset, geoapp)
        using the region, category and keyword filter defined.
        Only the resources matching the filter will be returned by default
        """
        _region_filter = self._define_or_filter(
            "regions", list(self.region.values_list("id", flat=True))
        )
        _category_filter = self._define_or_filter(
            "category", list(self.category.values_list("id", flat=True))
        )
        _keyword_filter = self._define_or_filter(
            "keywords", list(self.keyword.values_list("id", flat=True))
        )
        _group_filter = self._define_or_filter(
            "group", list(self.groups.values_list("id", flat=True))
        )
        _resource_type_filter = self._define_or_filter(
            "resource_type", filter(None, [self.resource_type])
        )

        _filters = list(filter(
            None,
            [
                _region_filter,
                _category_filter,
                _keyword_filter,
                _group_filter,
                _resource_type_filter,
            ],
        ))
        if not _filters:
            return qr
        return qr.filter(reduce(operator.and_, _filters))

    def _define_or_filter(self, key, iterable):
        match key:
            case "regions":
                queries = [Q(regions=value) for value in iterable]
            case "category":
                queries = [Q(category=value) for value in iterable]
            case "keywords":
                queries = [Q(keywords=value) for value in iterable]
            case "group":
                queries = [Q(group__groupprofile=value) for value in iterable]
            case "resource_type":
                queries = [Q(resource_type=value) for value in iterable]
            case _:
                return None
        if not queries:
            return None
        query = queries.pop()
        for item in queries:
            query |= item
        return query
