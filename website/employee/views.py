from django.shortcuts import render,get_object_or_404,redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def list_employees(request):
    employees=Employee.objects.all()
    context={
        'employees':employees,
    } 
    return render(request,'list_employee.html',context)

# ----------------------------------------------->
def employee_detail(request,id):
    employee=get_object_or_404(Employee,id=id)

    context={
        'employee':employee,
    }
    return render (request,'employee_detail.html',context)

# ----------------------------------------------->
def employee_create(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        salary=request.POST.get('salary')
        employee=Employee.objects.create(
            name=name , age=age , salary= salary
            )
        return redirect(list_employees)
    return render (request,'employee_creat.html')
# ----------------------------------------------->
def delete_employee(request,emp_id):
    employee=get_object_or_404(Employee,id=emp_id)
    employee.delete()

    return redirect ('list_employees')
# ----------------------------------------------->
def update_employee(request,emp_id): 
    employee=Employee.objects.get(id=emp_id)
    if request.method == "POST":
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect ('employee_detail',id=emp_id)
        
        
        
        
    form=EmployeeForm(instance=employee)
    context={
        'form':form,
    }
    return render (request,'update_employee.html',context)
