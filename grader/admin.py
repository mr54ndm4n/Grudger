from django.contrib import admin
from .models import Student, Problem, Testcase, Submission, ProblemCategorie, Lesson
# Register your models here.


class Testcase_In_Line(admin.StackedInline):
	model = Testcase
	extra = 4
	fields = ['case_input', 'case_output']

class ProblemAdmin(admin.ModelAdmin):
	fields = ['name', 'catagories', 'detail', 'total_score', 'difficulty', 'sample_input', 'sample_output', 'score_per_case']
	inlines = [Testcase_In_Line]

admin.site.register(Student),
admin.site.register(Submission),
admin.site.register(Problem, ProblemAdmin),
admin.site.register(ProblemCategorie),
admin.site.register(Lesson),
