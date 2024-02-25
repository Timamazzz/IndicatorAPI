from rest_framework import serializers

from contacts_app.models import Requisite


class RequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisite
        fields = '__all__'


class RequisiteGetActiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requisite
        exclude = ('is_active',)
