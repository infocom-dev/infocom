from django.contrib import admin

from backend.api.models import *


class AnswerInline(admin.TabularInline):
    model = AnswersOption


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


@admin.register(CustomerAnswer, Project, Customer, Stack, CustomUser,AnswersOption)
class AdminModels(admin.ModelAdmin):
    pass
