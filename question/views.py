from django.shortcuts import render,get_object_or_404,redirect
from .models import Question
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404
from django.core import serializers
from .forms import addform
from django.core.urlresolvers import reverse
@require_http_methods(['GET','POST'])
@require_GET
def list_ques(request):
	context={'listo':Question.objects.all()}
	return render(request,'question/list.html',context)

@login_required	
def  ques_add(request)	:
	if (request.method=='GET'):
		f=addform()
		return render(request,'question/add.html',{'f':f})
	if(request.method=='POST')	:
		f=addform(request.POST)
		if not f.is_valid:
			return render(request,'question/add.html',{'f':f})
		else:
			quesobj=f.save(commit=False)
			quesobj.created_by=request.user
			quesobj.save()
			return render(request,'question/posted.html')
@require_GET
def get_ques(request,pk):
	q=Question.objects.get(id=pk)
	if not q:
		raise Http404
	q=serializers.serialize('json',[q])	
	return HttpResponse(q,content_type='application/json')
@login_required	
@require_http_methods(['GET','POST'])
def ques_edit(request,id):
	quesobj=get_object_or_404(Question,id=id)
	if len(quesobj.answers_given.all())!=0:
		raise Http404
	if (request.method=='GET'):
		if (quesobj.created_by!=request.user):
			raise Http404()
		f=addform(instance=quesobj)
		return render(request,'question/edit.html',{'f':f,'id':id})
	if(request.method=='POST')	:
		if(quesobj.created_by!=request.user):
			raise Http404('you cant edit this')
		f=addform(request.POST,instance=quesobj)
		if not f.is_valid():
			return render(request,'question/edit.html',{'f':f,'id':id})	
		quesobj=f.save()
		return redirect(reverse('home',kwargs={'id':request.user.id}))
@login_required
@require_GET
def myques(request):
	list=Question.objects.filter(created_by=request.user)	
	return render(request,'question/myques.html',{'list':list})	
@login_required
@require_GET
def ans(request,id):
	ques_obj=Question.objects.get(id=id)
	answer_list=ques_obj.answers_given.all()
	return render(request,'question/answer.html',{'ques_obj':ques_obj,'answers':answer_list})
