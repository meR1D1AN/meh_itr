from django.contrib import admin

from .models import Esc, EscProblem, EscReplace, EscTO


@admin.register(Esc)
class EcsAdmin(admin.ModelAdmin):
    list_display = ("esc",)


@admin.register(EscProblem)
class EscProblemAdmin(admin.ModelAdmin):
    list_display = ("esc", "problem", "resolved", "create_at")


@admin.register(EscReplace)
class EscReplaceAdmin(admin.ModelAdmin):
    list_display = ("esc", "replace", "resolved", "create_at")


@admin.register(EscTO)
class EscTOAdmin(admin.ModelAdmin):
    list_display = ("esc", "create_at")
