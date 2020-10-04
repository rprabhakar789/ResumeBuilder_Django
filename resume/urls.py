from django.conf.urls import url
from .import views

urlpatterns = [
    # url(r'^$', ,),
	
    url(r'^resumeview', views.resumeView, name='resume_view'),
	url(r'',views.resumeFill, name = 'resumeFill'),
    url(r'^projectorjob', views.ProjectOrJob, name='projectorjob'),


]
