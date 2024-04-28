# def sumnumber (numbers):
#     return sum(numbers)
# print(sumnumber([1,5,6,22,2000]))
# -------------------------------------------------------------------------
# def sum_numbers (numbers):
#    numbers = numbers.split (' ')
#    new_numbers = []
#    for x in numbers :
#       new_numbers.append(int(x))
#    return sum (new_numbers)

# print (sum_numbers(input('enter your number you need to sum :')))
    
   

# def sum_number (numbers):
#       numbers = numbers.split (' ')
#       new = []
#       for x in numbers:
#        new.append(int(x))
#       return sum (new)


# print (sum_number(input('enter your number you need to sum :')))



# def sum_number (numbers):
#     numbers=numbers.split(' ')
#     new_number=[]
#     for x in numbers :
#         new_number.append (int(x))


#     return sum(new_number)

# print (sum_number(input('enter your number you need to sum :')))


# def hello (name,age,joptitle,*skills,**salary):
#     new= ''
#     for skill in skills :
#         new += skill + ' '

#     new2=''
#     for key,value in salary.items() :

#         new2 += key +' '+ f'{value}' + ' '
       
        
#     print(f'hello {name} your age is {age} your jop title is {joptitle} and your skills is {new} and {new2}' )


# hello('moustafa','26','programmer','gjango','javascript','python',salary=2000000,ponth=500000)


# print ('ahmed','mohamed','ali',sep='\n')
# print ('ahmed','mohamed', 'ali',sep='\t')
# print ('ahmed','mohamed', 'ali',sep='-------->')

# print ('omar',end= ' ')
# print ('ahmed')

# names= ['omar','ali','mohamed','moustafa']
# print ('  '.join(names))

while True:

    number=input ('enter your number')
    print(eval(number))