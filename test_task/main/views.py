from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status

from main.serializers import PollSerializer, QuestionSerializer
from main.models import Poll, Question


class TestView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        content = {
            "HI THERE"
        }
        return Response(content)


class PollsList(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

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
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

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
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data.get('text')
            choice_type = serializer.validated_data.get('choice_type')
            poll_id = serializer.validated_data.get('poll_id')
            # print(text, choice_type, poll_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsDetail(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

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
        queryset = Poll.objects.get(pk=pk)
        if queryset:
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
