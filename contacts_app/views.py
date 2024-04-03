from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from IndicatorAPI.utils.ModelViewSet import ModelViewSet
from contacts_app.models import RunningLine, Contact, CustomerLink, Requisite, PrivacyPolicy
from contacts_app.serializers.contact_serializers import ContactSerializer, ContactGetActiveSerializer
from contacts_app.serializers.customer_link_serializers import CustomerLinkSerializer, CustomerLinkListSerializer
from contacts_app.serializers.privacy_policy_serializers import PrivacyPolicySerializer, \
    PrivacyPolicyGetActiveSerializer
from contacts_app.serializers.requisite_serializers import RequisiteSerializer, RequisiteGetActiveSerializer
from contacts_app.serializers.running_line_serializers import RunningLineSerializer, RunningLineGetActiveSerializer


# Create your views here.
class RunningLineViewSet(ModelViewSet):
    queryset = RunningLine.objects.all()
    serializer_class = RunningLineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_list = {
        'get-active': RunningLineGetActiveSerializer
    }

    @action(detail=False, methods=['get'], url_path='get-active')
    def get_active(self, request):
        active_line = self.queryset.filter(is_active=True).first()
        if active_line:
            serializer = RunningLineGetActiveSerializer(active_line)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_list = {
        'get-active': ContactGetActiveSerializer,
    }

    @action(detail=False, methods=['get'], url_path='get-active')
    def get_active(self, request):
        active_contact = self.queryset.filter(is_active=True).first()
        if active_contact:
            serializer = ContactGetActiveSerializer(active_contact)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CustomerLinkViewSet(ModelViewSet):
    queryset = CustomerLink.objects.all()
    serializer_class = CustomerLinkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_list = {
        'list': CustomerLinkListSerializer,
    }


class RequisiteViewSet(ModelViewSet):
    queryset = Requisite.objects.all()
    serializer_class = RequisiteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_list = {
        'get-active': RequisiteGetActiveSerializer,
    }

    @action(detail=False, methods=['get'], url_path='get-active')
    def get_active(self, request):
        active_requisite = self.queryset.filter(is_active=True).first()
        if active_requisite:
            serializer = RequisiteGetActiveSerializer(active_requisite)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PrivacyPolicyViewSet(ModelViewSet):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_list = {
        'get-active': PrivacyPolicyGetActiveSerializer,
    }

    @action(detail=False, methods=['get'], url_path='get-active')
    def get_active(self, request):
        active_obj = self.queryset.filter(is_active=True).first()
        if active_obj:
            serializer = PrivacyPolicyGetActiveSerializer(active_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
