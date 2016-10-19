from django.conf import settings
from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	profile_pic = models.FileField(upload_to='grader/user/profile_pic', blank=True)
	nick_name = models.CharField(max_length=30, blank=True)
	score = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return self.nick_name

class ProblemCategorie(models.Model):
	name = models.CharField(max_length=30)
	# weight in percent
	weight = models.PositiveSmallIntegerField(default=0)
	start = models.DateTimeField('start')
	due = models.DateTimeField('due')
	def __str__(self):
		return self.name

class Problem(models.Model):
	catagories = models.ForeignKey(ProblemCategorie)
	name = models.CharField(max_length=30)
	difficulty = models.CharField(max_length=17)
	detail = models.TextField(blank=True, default='None')
	total_score = models.PositiveSmallIntegerField(default=0)
	sample_input = models.TextField(blank=True, default='None')
	sample_output = models.TextField(blank=True, default='None')
	# Score per Case
	score_per_case = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return self.name

class Testcase(models.Model):
	problem = models.ForeignKey(Problem)
	case_input = models.TextField(blank=True, default='')
	case_output = models.TextField(blank=True, default='')

class Submission(models.Model):

	student = models.ForeignKey(Student)
	# current = models.BooleanField(default=False)
	# submit_date = models.DateTimeField()
	problem = models.ForeignKey(Problem)
	user_file = models.FileField(storage=FileSystemStorage(location='progfile', base_url='progfile'))
	user_score = models.PositiveSmallIntegerField(default=0)
	result = models.CharField(max_length=30, default='')
	# T--TTT--, Timeout, ''
	def __str__(self):
		return (self.student.nick_name + ' : ' + self.problem.name)
		
class Lesson(models.Model):
	_id = models.PositiveSmallIntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	detail = models.TextField(blank=True)
	file1 = models.FileField(upload_to='media/lesson/', blank=True)
	file2 = models.FileField(upload_to='media/lesson/', blank=True)
	file3 = models.FileField(upload_to='media/lesson/', blank=True)
	file4 = models.FileField(upload_to='media/lesson/', blank=True)
	def __str__(self):
		return self.name

# class Announce(models.Model):
# 	title = models.CharField(max_length=50, blank=True)
# 	detail = models.TextField(blank=True)