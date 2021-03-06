from django.contrib import admin

from backend.api.models import *


# @admin.register(QuestionType)
# class PersonAdmin(admin.ModelAdmin):
#     pass


class AnswerInline(admin.TabularInline):
    model = AnswersOption


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]


@admin.register(CustomerAnswer, Project, Customer, Developer, CustomUser)
class AdminModels(admin.ModelAdmin):
    pass
