from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Problem, Submission, ProblemCategorie, Lesson
from django.contrib.auth.decorators import login_required
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
	print(data)
	return render(request, "syllabus.html", data)


@login_required(login_url='/login/')
def problem_list(request):
	data = {'page': 'problem'}
	data.update(basic_info(request))
	print(data)
	return render(request, "problem_list.html", data)


@login_required(login_url='/login/')
def problem(request):
	data = {'page': 'problem'}
	data.update(basic_info(request))
	print(data)
	return render(request, "problem.html", data)
