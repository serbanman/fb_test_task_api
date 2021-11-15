from django.utils import timezone
from rest_framework import serializers

from main.models import Poll, Question


class PollSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_blank=True, required=False)
    start_date = serializers.DateTimeField(default=timezone.now)
    end_date = serializers.DateTimeField(required=False, allow_null=True)
    description = serializers.CharField(max_length=255, allow_blank=True, required=False)

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class QuestionSerializer(serializers.Serializer):
    CHOICE_TYPES = (
        ('open', 'Ответ текстом'),
        ('single', 'Один вариант ответа'),
        ('multiple', 'Несколько вариантов ответа'),
    )

    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(
        max_length=255,
        allow_blank=True,
        required=False
    )
    choice_type = serializers.ChoiceField(
        choices=CHOICE_TYPES,
        allow_null=True,
        allow_blank=True
    )

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.choice_type = validated_data.get('choice_type', instance.choice_type)
        instance.save()
        return instance
