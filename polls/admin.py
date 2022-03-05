from django.contrib import admin
from .models import Question, Choice

# Register your models here. admin 관리
admin.site.register(Question)
admin.site.register(Choice)

