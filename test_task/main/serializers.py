from django.utils import timezone
from rest_framework import serializers

from main.models import Poll, Question, Answer


class PollSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_blank=True, required=False)
    start_date = serializers.DateTimeField(required=False, allow_null=True)
    end_date = serializers.DateTimeField(required=False, allow_null=True)
    description = serializers.CharField(max_length=255, allow_blank=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'

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
    poll = serializers.IntegerField(source='poll.id')
    class Meta:
        model = Question
        fields = ['text', 'choice_type', 'poll']

    def create(self, validated_data):
        try:
            text = validated_data['text']
            choice_type = validated_data['choice_type']
            poll_entry = Poll.objects.get(
                pk=validated_data['poll']['id']
            )
            return Question.objects.create(
                text=text,
                choice_type=choice_type,
                poll=poll_entry
            )
        except Exception as ex:
            print(ex)
            return None

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.choice_type = validated_data.get('choice_type', instance.choice_type)
        instance.save()
        return instance


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.IntegerField(source='question.id', required=True)
    answer_text = serializers.CharField(max_length=255, allow_blank=False, required=True)

    class Meta:
        model = Answer
        fields = [
            'question',
            'answer_text'
        ]
