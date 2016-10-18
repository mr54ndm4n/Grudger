from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Problem, Submission, ProblemCategorie, Lesson
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
	user = request.user
	page = 'dashboard'
	return render(request, "dashboard.html", {'user':user, 'page': page})

@login_required(login_url='/login/')
def setting(request):
	user = request.user
	page = 'setting'
	return render(request, "setting.html", {'user':user, 'page': page})


@login_required(login_url='/login/')
def gradebook(request):
	user = request.user
	page = 'gradebook'
	return render(request, "gradebook.html", {'user':user, 'page': page})


@login_required(login_url='/login/')
def syllabus(request):
	user = request.user
	page = 'syllabus'
	return render(request, "syllabus.html", {'user':user, 'page': page})


@login_required(login_url='/login/')
def problem_list(request):
	user = request.user
	page = 'problem'
	return render(request, "problem_list.html", {'user':user, 'page': page})


@login_required(login_url='/login/')
def problem(request):
	user = request.user
	page = 'problem'
	return render(request, "problem.html", {'user':user, 'page': page})
