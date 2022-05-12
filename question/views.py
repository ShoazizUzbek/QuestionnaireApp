import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from question.models import QuestionGuestSession, AnswerRecord, Guest, Question, Questionnaire
from question.serializers import SessionSerializer, RecordAnswer, QuestionnaireSerializer, QuestionSerializer, \
    GuestSerializer


class AddQuestionnaire(APIView):

    def post(self, request, format=None):
        serializer = QuestionnaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddQuestion(APIView):

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddGuest(APIView):

    def post(self, request, format=None):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GuestList(APIView):

    def get(self, request, format=None):
        guests = Guest.objects.all(
        ).values('username', 'id')
        return Response(
            guests
        )

class QuestionnaireList(APIView):

    def get(self, request):
        questions = Questionnaire.objects.all(
        ).values('name', 'id')
        return Response(
            questions
        )

class QuestionList(APIView):

    def get(self, request, questionnaire_id):
        questions = Question.objects.filter(
            questionnaire_id=questionnaire_id
        ).values('text_question', 'id')
        return Response(
            questions
        )


class StartSession(APIView):
    '''
    This is API for starting questionnaire session
    This API saves the starting time of session
    '''
    def post(self, request,):
        serializer = SessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        current_time = datetime.datetime.now()
        validated_data['started_time'] = current_time
        sessoion = QuestionGuestSession.objects.create(
            **validated_data
        )
        return Response(
            {
                'session_id': sessoion.id,
                'data': f'Session started at {current_time}'
            }
        )


class AnswerPage(APIView):

    '''
    This API for answering of each question
    '''

    def post(self, request,):
        serializer = RecordAnswer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        session_id  = validated_data.get('session_id')
        question_id  = validated_data.get('question_id')
        answer = validated_data.get('answer')
        current_time = datetime.datetime.now()#submitted time of each question
        AnswerRecord.objects.create(
            question_id=question_id,
            session_id=session_id,
            text_answer=answer,
            submitted_time=current_time,
        )
        return Response({'data': 'You submitted the answer'})



class EngagementView(APIView):

    '''
    This API give engagement
    '''

    def get(self, request, session_id):
        session = QuestionGuestSession.objects.get(pk=session_id)
        question_count = session.questionnaire.questions.all().count()
        started_time = session.started_time
        list_times = []
        records = AnswerRecord.objects.filter(session_id=session_id)
        previous_time = started_time
        overall = 0
        for record in records:
            duration = record.submitted_time - previous_time
            list_times.append(
                {
                    'quesiton_id': record.question_id,
                    'answer': record.text_answer,
                    'spent_time': duration.seconds
                }
            )
            previous_time = record.submitted_time
            overall = duration.seconds

        return Response(
            {
                'Questions': question_count,
                'Overall spent time': overall,
                'All spent time': list_times
        })