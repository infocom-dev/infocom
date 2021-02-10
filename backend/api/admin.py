from django.contrib import admin

from backend.api.models import *


@admin.register(Question, QuestionType, Answer)
class PersonAdmin(admin.ModelAdmin):
    pass
