emplyees=[]

while True:
    print('1)Add new employee')
    print('2) Print all employees')
    print('3) Delete by age')
    print('4) Update Salary by name')
    print('5) End the program')
    user_input = input("Enter your choice from 1 to 5:").split()

    for choice in user_input:
        if choice == '1':
            print('Enter employee data')
            name=input('enter employee name:')
            age=int(input('Enter the age:'))
            salary=int(input('Enter the salary:'))
            emplyees.append({'name': name, 'age': age , 'salary':salary})
            
            print('Employee added successfully!')
        elif choice == '2':
            if not emplyees:
                print('No employees at the moment!')
            else:
                print('**Employees list**')
                for employee in emplyees:
                    print(f"employee:{employee['name']} has {employee['age']} and his salary is {employee['salary']}")
        elif choice == '3':
            f=int(input('enter age from:'))
            t=int(input('enter age to:'))
            emplyees=[emp for emp in emplyees if not (f <= emp['age']<= t)] 
            print ('employee deleted succssfully')
        elif choice == '4':
            employee_name=input('enter employee name:')
            new_salary=float(input('enter new salary:'))  
            for emp in emplyees:
                if emp['name'] == employee_name:
                    emp.update({'salary':new_salary})
                    print ('salary is updated!')
                else:
                    print('Error: No employee with such a name')
        elif choice =='5':
            print ('exit the program.')
            break
        else:
            print("Invalid input.Try again.")
    if '5' in choice:
        break
              
            
            






    
    

