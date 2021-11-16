from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.models import AnonymousUser, User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, exceptions
import datetime
import pytz

from main.serializers import PollSerializer, QuestionSerializer, AnswerSerializer

from main.models import Poll, Question, RespondentUser, Answer


class TestView(APIView):
    # placeholder
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        content = {
            "HI THERE"
        }
        return Response(content)


class BasicAuth(APIView):

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)

        return Response(user.id)

class PollsList(APIView):
    # get the list of polls or create an entry
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        queryset = Poll.objects.all()
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PollsDetail(APIView):
    # retrieve, update or delete the poll entry based on specific pk
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        queryset = Poll.objects.get(pk=pk)
        serializer = PollSerializer(queryset)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        queryset = Poll.objects.get(pk=pk)
        serializer = PollSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = Poll.objects.get(pk=pk)
        if queryset:
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class QuestionsList(APIView):
    # get the list of questions or create an entry
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            # text = serializer.validated_data.get('text')
            # choice_type = serializer.validated_data.get('choice_type')
            # poll_id = serializer.validated_data.get('poll_id')
            # print(text, choice_type, poll_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsDetail(APIView):
    # create, retrieve, update or delete the question entry based on specific pk
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        queryset = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(queryset)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        queryset = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = Question.objects.get(pk=pk)
        if queryset:
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ActivePolls(APIView):
    # get the list of all the active polls in which the end_date did not come yet
    def get(self, request):
        queryset = Poll.objects.filter(end_date__gte=datetime.datetime.now(tz=pytz.UTC))
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)


class LeaveAnAnswer(APIView):

    def post(self, request):
        if request.user == AnonymousUser():
            # if user is anonymous, we get or create the RespondentUser entry
            # based on the 'localauth' cookie

            user, created = RespondentUser.objects.get_or_create(
                session_cookies=request.COOKIES.get('localauth')
            )

            serializer = AnswerSerializer(data=request.data)
            if serializer.is_valid():
                # and then creating the Answer entry, based on RespondentUser entry and
                # the data from the request

                question_id = serializer.validated_data.get('question')['id']
                answer_text = serializer.validated_data.get('answer_text')

                question = Question.objects.get(pk=question_id)

                answer = Answer.objects.get_or_create(
                    question=question,
                    answer_text=answer_text,
                    respondent_user=user
                )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            # if user is authorized, we get or create an entry of RespondentUser for him
            local_user = User.objects.get(pk=request.user.id)
            user, created = RespondentUser.objects.get_or_create(
                authorized_credentials=local_user
            )

            serializer = AnswerSerializer(data=request.data)
            if serializer.is_valid():
                # and then creating the Answer entry, based on RespondentUser entry and
                # the data from the request

                question_id = serializer.validated_data.get('question')['id']
                answer_text = serializer.validated_data.get('answer_text')

                question = Question.objects.get(pk=question_id)

                answer = Answer.objects.get_or_create(
                    question=question,
                    answer_text=answer_text,
                    respondent_user=user
                )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswersList(APIView):
    # get the list of all answers by the RespondentUser
    def get(self, request, pk, format=None):
        queryset = Answer.objects.filter(respondent_user=pk)
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)
