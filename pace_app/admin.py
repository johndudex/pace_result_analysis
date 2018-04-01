from django.contrib import admin
from pace_app.models import Subject, Faculty, Department


class SubjectAdmin(admin.ModelAdmin):
    pass


class FacultyInline(admin.TabularInline):
    model = Faculty.subject.through


class FacultyAdmin(admin.ModelAdmin):
    inlines = [FacultyInline, ]


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Faculty, FacultyAdmin)

admin.site.register(Department, DepartmentAdmin)
