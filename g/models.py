from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    text = models.CharField(max_length=400)
    semester = models.IntegerField(default=1)
    major = models.CharField(max_length=400)

    def __unicode__(self):
        return str(self.semester) + " " + self.major + " " + self.text


class Question(models.Model):
    course = models.ForeignKey(Course)
    posted_by = models.ForeignKey(User)
    text = models.CharField(max_length=400)
    date = models.DateTimeField('date posted')

    def __unicode__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    course = models.ForeignKey(Course)
    posted_by = models.ForeignKey(User)
    date = models.DateTimeField('date posted')
    text = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.text


class Favorites(models.Model):
    user = models.OneToOneField(User)
    question = models.OneToOneField(Question)

    def __unicode__(self):
        return str(self.question.text)