from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Problem, Submission, ProblemCategorie, Lesson
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
	return HttpResponse("Hi")

@login_required(login_url='/login/')
def setting(request):
	return HttpResponse("Setting")

@login_required(login_url='/login/')
def gradebook(request):
	return HttpResponse("Setting")

@login_required(login_url='/login/')
def syllabus(request):
	return HttpResponse("Setting")

@login_required(login_url='/login/')
def problem_list(request):
	return HttpResponse("Setting")

@login_required(login_url='/login/')
def problem(request):
	return HttpResponse("Setting")