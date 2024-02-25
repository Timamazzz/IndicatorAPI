from django.urls import path, include
from rest_framework.routers import DefaultRouter

from contacts_app.views import RunningLineViewSet, ContactViewSet, CustomerLinkViewSet, RequisiteViewSet

router = DefaultRouter()
router.register(r'running-lines', RunningLineViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'customer-links', CustomerLinkViewSet)
router.register(r'requisites', RequisiteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
