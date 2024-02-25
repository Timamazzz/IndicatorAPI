from rest_framework import serializers

from contacts_app.models import RunningLine, RunningText


class RunningLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningLine
        fields = '__all__'


class RunningTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningText
        fields = ('text', )


class RunningLineGetActiveSerializer(serializers.ModelSerializer):
    running_texts = RunningTextSerializer(many=True, read_only=True)

    class Meta:
        model = RunningLine
        fields = ('name', 'running_texts', )
