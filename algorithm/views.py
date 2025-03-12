from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question, Answer
from .serializer import QuestionSerializer, AnswerSerializer


class QuestionListView(APIView):
    def get(self, request, id=None):
        if id is None:
            _questions = Question.objects.all()
            serializer = QuestionSerializer(_questions, many=True)
        else:
            _question = Question.objects.get(id=id)
            serializer = QuestionSerializer(_question)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully create question'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        _question = Question.objects.get(id=id)
        _question.delete()
        return Response({"message": "Successfully delete question"}, status=status.HTTP_200_OK)
    
    def put(self, request, id=None):
        _question = Question.objects.get(id=id)
        data = request.data

        if 'subject' in data and data["subject"] != '':
            _question.subject = data["subject"]
        if 'number' in data and data["number"] != '':
            _question.number = data["number"]
        _question.save()

        return Response({'message': "Successfully update question"}, status=status.HTTP_200_OK)