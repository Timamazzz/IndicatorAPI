from wagtail.api.v2.router import WagtailAPIRouter

from project_app_v2.views import ProjectPageViewSet

api_router = WagtailAPIRouter('wagtailapi')
api_router.register_endpoint('projects', ProjectPageViewSet)

