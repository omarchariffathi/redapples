from django.conf.urls import patterns, url

from g import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.questions, name='questions'),
    url(r'^my_questions/$', views.my_questions, name='my_questions'),
    url(r'^my_answers/$', views.my_answers, name='my_answers'),
    url(r'^add_answer/$', views.add_answer, name="add_answer"),
    url(r'^add_question/$', views.add_question, name="add_question"),
)