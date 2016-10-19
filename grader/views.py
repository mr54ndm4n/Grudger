from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from .models import Student, Problem, Submission, ProblemCategorie, Lesson
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import time
import datetime
from django.utils import timezone
# Create your views here.

def basic_info(request):
	user = request.user
	try:
		student = Student.objects.get(user = request.user)
	except:
		student = Student(user=request.user)
		student.nick_name = user.username
		student.save()
	return {'user':user, 'student':student}

@login_required(login_url='/login/')
def dashboard(request):
	data = {'page': 'dashboard'}
	data.update(basic_info(request))
	print(data)
	return render(request, "dashboard.html", data)

@login_required(login_url='/login/')
def setting(request):
	data = {'page': 'setting'}
	data.update(basic_info(request))
	print(data)
	return render(request, "setting.html", data)


@login_required(login_url='/login/')
def gradebook(request):
	data = {'page': 'gradebook'}
	data.update(basic_info(request))
	print(data)
	return render(request, "gradebook.html", data)


@login_required(login_url='/login/')
def syllabus(request):
	data = {'page': 'syllabus'}
	data.update(basic_info(request))
	data['lesson_list'] = Lesson.objects.all()
	print(data)
	return render(request, "syllabus.html", data)


@login_required(login_url='/login/')
def problem_list(request):
	user = request.user
	student = Student.objects.get(user = request.user)
	problem_list = Problem.objects.all()
	sub_prob = []
	for problem in problem_list:
		try:
			ps = Submission.objects.get(student = student, problem = problem)
		except:
			ps = Submission(student = student, problem = problem)
			ps.save()
		print('Active: ' + str(problem.catagories.due >= timezone.now() and problem.catagories.start <= timezone.now()))
		active = problem.catagories.due >= timezone.now() and problem.catagories.start <= timezone.now()
		sub_prob.append({'problem': problem, 'submission': ps, 'active': active})
	return render(request, 'problem_list.html', {'user': user, 'student': student, 'sub_prob_list': sub_prob})


@login_required(login_url='/login/')
def problem(request):
	data = {'page': 'problem'}
	data.update(basic_info(request))
	print(data)
	return render(request, "problem.html", data)
