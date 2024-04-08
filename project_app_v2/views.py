from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.urls import reverse, path
from rest_framework.renderers import JSONRenderer
from wagtail.api.v2.views import PagesAPIViewSet

from project_app_v2.models import ProjectPage


# Create your views here.
class ProjectPageViewSet(PagesAPIViewSet):
    renderer_classes = [JSONRenderer]
    name = "projectPage"
    model = ProjectPage

    detail_only_fields = []
    body_fields = ['id']
    meta_fields = []

    def detail_view(self, request, pk=None, slug=None):
        param = pk
        if slug is not None:
            self.lookup_field = 'slug'
            param = slug
        try:
            return super().detail_view(request, param)
        except MultipleObjectsReturned:
            return redirect(
                reverse('wagtailapi:pages:listing') + f'?{self.lookup_field}={param}'
            )

    @classmethod
    def get_urlpatterns(cls):
        """
        This returns a list of URL patterns for the endpoint
        """
        return [
            path("", cls.as_view({"get": "listing_view"}), name="listing"),
            path("<slug:slug>/", cls.as_view({"get": "detail_view"}), name="detail"),
            path("find/", cls.as_view({"get": "find_view"}), name="find"),
        ]