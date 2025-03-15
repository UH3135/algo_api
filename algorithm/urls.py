from django.urls import path
from .views import QuestionListView, AnswerListView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name="question-list"),
    path('questions/<int:id>/', QuestionListView.as_view(), name="question-detail"),
    path('answers/', AnswerListView.as_view(), name='answer-list'),
]