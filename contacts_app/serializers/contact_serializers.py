from rest_framework import serializers

from contacts_app.models import Contact, ContactsLink


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactsLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsLink
        exclude = ('contact',)


class ContactGetActiveSerializer(serializers.ModelSerializer):
    urls = ContactsLinkSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        exclude = ('is_active',)
