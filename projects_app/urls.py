from django.urls import path, include
from rest_framework.routers import DefaultRouter

from projects_app.views import ProjectViewSet

router = DefaultRouter()
router.register(r'', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
