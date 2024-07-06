
from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.list_employees,name='list_employees' ),
    path('remove-employee/<int:emp_id>/',views.delete_employee,name='delete_employee' ),
    path('create/',views.employee_create,name='employee_create'),
    path('employee/<int:id>/',views.employee_detail,name='employee_detail' ),
    path('update/<int:emp_id>/',views.update_employee,name='update_employee'),  
    
    
    
    

]