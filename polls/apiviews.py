from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from .models import Question
from .serializers import QuestionSerializer


@api_view(['GET', 'POST'])
def questions_view(request):
    if request.method == 'GET':
        # questions = []
        # for question in Question.objects.all():
        #     question_representation = {'question_text': question.question_text, 'pub_date': question.pub_date.strftime("%Y-%m-%d")}
        #     questions.append(question_representation)
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
        #return HttpResponse(json.dumps(questions), content_type='application/json')
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            # question_text = serializer.data['question_text']
            # pub_date = serializer.data['pub_date']
            # Question.objects.create(question_text=question_text, pub_date=pub_date)
            Question.objects.create(**serializer.validated_data)
            return Response("Question created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)