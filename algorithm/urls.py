from django.urls import path
from .views import QuestionListView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name="question-list"),
    path('questions/<int:id>/', QuestionListView.as_view(), name="question-detail"),
]