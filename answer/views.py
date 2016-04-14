from django.shortcuts import render,get_object_or_404
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from question.models import Question
from .forms import postansform
from .models import answer
from django.http import Http404


# Create your views here.
@require_http_methods(['GET','POST'])
@login_required
def add(request,id):
	if(request.method=='GET'):
		f=postansform()
		return render(request,'answer/add.html',{'f':f,'id':id})
	if(request.method=='POST')	:
		f=postansform(request.POST)
		if not f.is_valid():
			return render(request,'answer/add.html',{'f':f,'id':id})
		ansobj=f.save(commit=False)	
		ansobj.created_by=request.user
		ansobj.question_answered=get_object_or_404(Question,id=id)
		ansobj.save()
		return render(request,'answer/posted.html')
@login_required
@require_http_methods(['GET','POST'])
def edit(request,id)	:
	ansobj=get_object_or_404(answer,id=id)
	if (request.method=='GET'):
		if (request.user==ansobj.created_by):
			f=postansform(instance=ansobj)
			return render(request,'answer/edit.html',{'f':f,'ansobj':ansobj})
		else:
			raise Http404	
	if(request.method=='POST')		:
		if(request.user==ansobj.created_by):
			f=postansform(request.POST,instance=ansobj)
			if not f.is_valid():
				return render(request,'answer/edit.html',{'f':f,'ansobj':ansobj})
			ansobj=f.save()
			return render(request,'answer/posted.html')






