from django.db import models
from account.models import MyUser

# Create your models here.
class Question(models.Model):
	title=models.CharField(max_length=100)
	body=models.CharField(max_length=1000,blank=True)
	created_by=models.ForeignKey(MyUser,related_name='questions_created')
	upvoted_by=models.ManyToManyField(MyUser,related_name='questions_upvoted',blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
