from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    number = models.IntegerField(null=True)
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    content = models.TextField()
