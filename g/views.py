from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from g.models import Question, Answer, Course, Favorites
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.sessions.models import Session

# Create your views here.


def home(request):
    return render(request, "home.html", {})


def index(request):
    if request.user.is_anonymous():
        return render(request, "500.html", {})
    else:
        latest_question_list = Question.objects.all().order_by('-date')
        latest_answer_list = Answer.objects.all()
        template = 'dash.html'
        context = {
            'latest_question_list': latest_question_list,
            'latest_answer_list': latest_answer_list,
            'first': request.user.first_name,
            'last': request.user.last_name,
        }
        return render(request, template, context)


def questions(request, question_id):
    if request.user.is_anonymous():
        return render(request, "500.html", {})
    else:
        q = Question.objects.get(id=question_id)
        answers_list = Answer.objects.filter(question=q)
        ques = q

        template = 'question.html'
        context = {
            'answers_list': answers_list,
            'question_id': question_id,
            'ques': ques,
            'first': request.user.first_name,
            'last': request.user.last_name,
        }
        return render(request, template, context)


def my_answers(request):
    if request.user.is_anonymous():
        return render(request, "500.html", {})
    else:
        answers_list = Answer.objects.filter(posted_by=request.user)
        questions_list = Question.objects.filter(id=Answer.objects.filter(posted_by=request.user).values('question'))

        print '\n' + str(answers_list)
        print '\n' + str(questions_list)

        template = 'my_answer.html'
        context = {
            'answers_list': answers_list,
            'questions_list': questions_list,
            'first': request.user.first_name,
            'last': request.user.last_name,
        }
        return render(request, template, context)


def my_questions(request):

    if request.user.is_anonymous():
        return render(request, "500.html", {})
    else:
        print request.user
        questions_list = Question.objects.filter(posted_by=request.user)
        answers_list = Answer.objects.filter(question=Question.objects.filter(posted_by=request.user))

        template = 'my_question.html'
        context = {
            'questions_list': questions_list,
            'answers_list': answers_list,
            'first': request.user.first_name,
            'last': request.user.last_name,
        }
        return render(request, template, context)


def add_answer(request):
    if request.user.is_anonymous():
        return render(request, "500.html", {})
    else:
        a = request.POST.get('answer', '')
        ques = request.POST.get('ques_id', '')
        if a != '':
            q = Question.objects.get(id=ques)
            u = request.user
            answer = Answer(question=q, text=a, date=timezone.now(), course=q.course, posted_by=u)
            answer.save()
            return HttpResponseRedirect("/g/")
        else:
            return HttpResponseRedirect("/g/")


def add_question(request):
    if request.user.is_anonymous():
        return render(request, "500.html", {})
    else:
        a = request.POST.get('question', '')
        if a != '':
            u = request.user
            q = Question(text=a, date=timezone.now(), course=Course.objects.get(id=1), posted_by=u)
            q.save()
            return HttpResponseRedirect("/g/")
        else:
            return HttpResponseRedirect("/g/")