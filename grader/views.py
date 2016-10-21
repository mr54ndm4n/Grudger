import datetime
import subprocess
import time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.utils import timezone
from .models import Student, Problem, Submission, ProblemCategorie, Lesson
from .forms import ProblemForm, Profile_PicForm
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
	user = request.user
	student = Student.objects.get(user = request.user)
	error_message = ''
	if request.method == 'POST':
		if 'profilepic' in request.POST:
			form = Profile_PicForm(request.POST, request.FILES)
			pic = request.FILES['profile_pic']
			student.profile_pic = pic
			student.save()
			print('profilepic')
		elif 'general' in request.POST:
			firstname = request.POST.get('firstname', False)
			lastname = request.POST.get('lastname', False)
			email = request.POST.get('email', False)
			nick = request.POST.get('nick', False)
			user.first_name = firstname
			user.last_name = lastname
			user.email = email
			student.nick_name = nick
			student.save()
			user.save()
			print(firstname + ' ' + lastname + '  ' + email)
		elif 'password-changed' in request.POST:
			old = request.POST.get('old-pass', False)
			new1 = request.POST.get('new-pass1', False)
			new2 = request.POST.get('new-pass2', False)
			if user.check_password(old) == True:
				if new1 == new2:
					user.set_password(new1)
					user.save()
					return HttpResponseRedirect('/login/')
				else:
					error_message = 'New password do not match'
			else:
				error_message = 'Your old password is not correct'
	form = Profile_PicForm()
	return render(request, 'setting.html', {'user': user, 'student': student, 'error_message': error_message, 'page': 'setting', 'form': form,})


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
	return render(request, 'problem_list.html', {'user': user, 'student': student, 'sub_prob_list': sub_prob, 'page': 'problem'})


@login_required(login_url='/login/')
def problem(request, problem_id):
	user = request.user
	student = Student.objects.get(user = user)
	problem = Problem.objects.get(id = problem_id)
	error_message = ''
	active = problem.catagories.due >= timezone.now() and problem.catagories.start <= timezone.now()
	if not active:
		error_message = 'Now This Problem Is Not Active'
	try:
		mysub = Submission.objects.get(student = student, problem = problem)
	except:
		mysub = Submission(student = student, problem = problem)
		create_new = 1
	timeout = 0
	if request.method == 'POST' and active == True:
		form = ProblemForm(request.POST, request.FILES)
		if form.is_valid():
			student.score -= mysub.user_score
			mysub.user_score = 0
			testcases = problem.testcase_set.all()
			ufile = request.FILES['user_file']
			mysub.user_file = ufile
			mysub.save()
			print('Compiling: ' + mysub.user_file.name)
			task0 = subprocess.Popen("gcc progfile/" + mysub.user_file.name + " -o opt")
			task0.wait(timeout=None)
			# if compile not error V
			if task0.returncode == 0: 
				mysub.result = ''
				for case in testcases:
					task1 = subprocess.Popen("opt", stdout=subprocess.PIPE, stdin=subprocess.PIPE)
					# task1.stdin.write(case.case_input.encode('utf-8'))
					try:
						out, err = task1.communicate(input=case.case_input.encode('utf-8'), timeout = 3)
					# If it's timeout
					except:
						print('It\'s Timeout')
						mysub.result = 'Timeout'
						mysub.user_score = 0
						task1.kill()
						chk_0 = task0.poll()
						while chk_0 == None:
							task0.terminate()
							time.sleep(1)
							chk_0 = task1.poll()
						print('Poll0: ->' + str(task0.poll()))
						chk_1 = task1.poll()
						while chk_1 == None:
							task1.terminate()
							time.sleep(1)
							chk_1 = task1.poll()
						print('Poll1: ->' + str(task1.poll()))
						break
					print(repr(out.decode('ascii').replace('\r', ''))+'\n'+repr(case.case_output.replace('\r', '')))
					if(repr(out.decode('ascii').replace('\r', '')) == repr(case.case_output.replace('\r', ''))):
						mysub.result += 'P '
						mysub.user_score += problem.score_per_case
					else:
						mysub.result +='- '
					task1.terminate()
					task1.kill()

				# Killing task_0
				chk_0 = task0.poll()
				while chk_0 == None:
					task0.terminate()
					time.sleep(1)
					chk_0 = task0.poll()
				print('Task0.poll: ' + str(task0.poll()) + '\n')
				# Killing Task_1
				chk_1 = task1.poll()
				while chk_1 == None:
					task1.terminate()
					time.sleep(1)
					chk_1 = task1.poll()
				print('Task1.poll: ' + str(task1.poll()))
			# if compile Error
			else:
				mysub.result = 'Compile Error'
				mysub.user_score = 0
			print(mysub.result+'\n'+str(mysub.user_score)+'/'+str(problem.total_score))
			student.score += mysub.user_score
			student.save()
			mysub.save()
			return HttpResponseRedirect('/grader/problem/'+problem_id+'/')
	else:
		form = ProblemForm()
		#Remove OPT
		# task3 = subprocess.Popen("rm -f opt.exe", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		# task3.wait(timeout=None)
	return render(request, 'problem.html', {'user': user, 'problem': problem, 'form': form, 'student': student, 'mysub': mysub, 'page': 'problem'})
