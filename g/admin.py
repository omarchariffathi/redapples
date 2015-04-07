from django.contrib import admin
from g.models import Question, Answer, Course


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Course)