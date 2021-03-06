from django.contrib import admin

from backend.api.models import *


@admin.register(QuestionType)
class PersonAdmin(admin.ModelAdmin):
    pass

class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]