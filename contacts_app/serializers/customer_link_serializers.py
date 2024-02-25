from rest_framework import serializers

from contacts_app.models import CustomerLink


class CustomerLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLink
        fields = '__all__'


class CustomerLinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLink
        fields = ('name', 'url')

