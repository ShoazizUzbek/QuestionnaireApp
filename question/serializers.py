from rest_framework import serializers

from question.models import Questionnaire, Question, Guest


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = [
            'name',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'questionnaire',
            'text_question'
        ]

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = [
            'username',
        ]

class SessionSerializer(serializers.Serializer):

    questionnaire_id = serializers.IntegerField()
    guest_id = serializers.IntegerField()

class RecordAnswer(serializers.Serializer):
    session_id = serializers.IntegerField()
    answer = serializers.CharField()
    question_id = serializers.IntegerField()