from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render, redirect
from django.urls import reverse, path

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from wagtail.api.v2.views import PagesAPIViewSet

from project_app_v2.models import ProjectPage, UniqueProjectViewPage
from project_app_v2.serializers import ProjectViewPageSerializer



# Create your views here.
class ProjectPageViewSet(PagesAPIViewSet):
    renderer_classes = [JSONRenderer]
    name = "projectPage"
    model = ProjectPage
    base_serializer_class = ProjectViewPageSerializer
    detail_only_fields = []
    body_fields = ['id', 'views']
    meta_fields = []

    def detail_view(self, request, pk=None, slug=None):
        param = pk
        if slug is not None:
            self.lookup_field = 'slug'
            param = slug
        try:
            instance = self.get_object()
            ip_address = self.request.META.get('REMOTE_ADDR')
            user_agent = self.request.META.get('HTTP_USER_AGENT')

            UniqueProjectViewPage.objects.get_or_create(
                project=self.get_object(),
                ip_address=ip_address,
                user_agent=user_agent
            )
            serializer = self.get_serializer(instance)

            return Response(serializer.data)

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