from django.urls import path, include
from rest_framework.routers import DefaultRouter

from projects_app.views import ProjectViewSet, ProjectDiscussAPIView

router = DefaultRouter()
router.register(r'', ProjectViewSet)

urlpatterns = [
    path('discuss/', ProjectDiscussAPIView.as_view()),
    path('', include(router.urls)),
]
