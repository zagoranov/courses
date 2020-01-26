from django.contrib import admin

from .models import Lector, Course, Lesson


@admin.register(Lector)
class LectorAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', "date_started", 'full_name'
    list_display_links = 'id', 'full_name'

#admin.site.register(Lector, LectorAdmin)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    def description_short(self, obj: Course):
        if len(obj.description) <= 30:
            return obj.description
        return f'{obj.description[:30]}'

    list_display = 'id', 'name', 'description_short', 'lector'
    list_display_links = 'id', 'name'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):

    def description_short(self, obj: Lesson):
        if len(obj.description) <= 30:
            return obj.description
        return f'{obj.description[:30]}'

    list_display = 'id', 'name', 'date_start', 'description_short', 'course'
    list_display_links = 'id', 'name'
