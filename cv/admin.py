from django.contrib import admin
from cv.models import Employee, CVmaker

# Register your models here.

@admin.register(CVmaker)
class CVmakerAdmin(admin.ModelAdmin):
    model = CVmaker

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee

