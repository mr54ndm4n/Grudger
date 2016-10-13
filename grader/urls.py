from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^setting', views.setting),
	url(r'^gradebook', views.gradebook),
	url(r'^syllabus', views.syllabus),
	url(r'^problem/(?P<problem_id>[0-9]+)/$', views.problem),
	url(r'^problemlist/$', views.problem_list),
	url(r'^$', views.dashboard),
]