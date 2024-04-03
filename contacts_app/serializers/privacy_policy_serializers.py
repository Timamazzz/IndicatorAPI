from rest_framework import serializers

from contacts_app.models import PrivacyPolicy


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class PrivacyPolicyGetActiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivacyPolicy
        fields = ('text', )

