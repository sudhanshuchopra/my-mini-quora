from django.db import models
from account.models import MyUser
from question.models import Question
class answer(models.Model):
	created_by=models.ForeignKey(MyUser,related_name='answers_created')
	question_answered=models.ForeignKey(Question,related_name='answers_given')
	body=models.TextField(max_length=1000)
	created_on=models.DateTimeField(auto_now_add=True)