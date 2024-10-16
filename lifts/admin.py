from django.contrib import admin
from django.utils.html import format_html
from lifts.models import Building, Problem, Elevator, Replacement, TO


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("address", "elevators_list")

    def elevators_list(self, obj):
        elevators = obj.elevators.all()
        if elevators:
            return format_html("<br>".join([str(elevator) for elevator in elevators]))
        return "Нет лифтов"

    elevators_list.short_description = "Лифты"


@admin.register(Elevator)
class ElevatorAdmin(admin.ModelAdmin):
    list_display = ("elevator", "buildings_list")

    def buildings_list(self, obj):
        buildings = obj.buildings.all()
        if buildings:
            return format_html("<br>".join([str(building) for building in buildings]))
        return "Нет зданий"

    buildings_list.short_description = "Здания"


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ("buildings", "elevator", "problem", "resolved")
    list_filter = ("buildings", "elevator", "resolved")
    list_display_links = ("elevator",)
    search_fields = ("problem",)


@admin.register(Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ("buildings", "elevator", "info_problem", "resolved")
    list_filter = ("buildings", "elevator", "resolved")
    list_display_links = ("elevator",)
    search_fields = ("info_problem",)


@admin.register(TO)
class TOAdmin(admin.ModelAdmin):
    list_display = ("building", "elevator", "date")
    list_display_links = ("elevator",)
    list_filter = ("building", "elevator", "date")
