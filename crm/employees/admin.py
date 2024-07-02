from django.contrib import admin
from.models import employee
# Register your models here.
# class Employee_admin(admin.ModelAdmin):
#     list_display = ['id','name','age','salary']
# admin.site.register(employee,Employee_admin)
@admin.register(employee)
class employeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','salary']



