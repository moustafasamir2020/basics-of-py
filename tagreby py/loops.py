# names=['rami','omar','mohamed']
# # print (names)

# num=1
# for name in names:
#     # print('employee:',name)  
#     print(f'employee {num} : {name}')
#     # num=num+
#     num += 1


# numbers=[10,20,30,40,50,60,70]

# for number in numbers:
#     print (number)

# calender=('sat','sun','mon','tu','we')

# for days in calender :
#     print (days)


# name= "moustafa samir"

# for i in name :
#     print (i)

#nested loop
# names=['rami','omar','mohamed']

# for name in names :
#     print (name)
#     for i in name : 
#         print (i)



# employee={
#     'name' :'mohamed',
#     'age' : '30',
#     'salary' : '45454',
# }
# # print (employee)
# # for key in employee :
# # #    print (key)
# #     print (employee[key])

# # for value in employee.values():
# #     print (value)

# # for key in employee.keys() : 
# #     print(key)


# # for key in employee :
# #     print (key)

# # for key,value in employee.items():
# #     print (f'{key}------->{value}')




# employees={
#     'employee1':{
#                 'name' :'mohamed',
#                 'age' : 30,
#                 'salary' : 45454, 
#                 },

#     'employee2':{
#                 'name' :'ahmed',
#                 'age' : 29,
#                 'salary' : 43334, 
#                 } ,   
#      'employee3':{
#                 'name' :'ali',
#                 'age' : 25,
#                 'salary' : 3574, 
#                 }  ,                 
# }

# for mainkey,mainvalue in employees.items():
#     # for i in employee.values() :
#         print (mainkey,":")
#         for childkey,childvalue in mainvalue.items():
#                 print (f'{childkey}----------->{childvalue}')

# names=['rami','omar','mohamed']
# print(len(names))

# 
# x=0

# while x<len(names):
#     print(names[x])
#     x +=1
# for i in names :
#     print (i)

# name='omar mohamed'

# x=0

# while x<len(name):
#     print(name[x])
#     x+=1
#     break


# for i in name :
#     print (i)

# 
# names=['rami','omar','mohamed']

# x=0
# y=0

# while x<len(names):
#     print (names[x])
#     x+=1
#     while y<len([x]):
#         print (x [y])
#         y+=1
# for name in names:
#     for i in name:
#         print (i)


# list=['ramy ','mohamed','hassn','moustafa']
# list.reverse()
# num=1
# for i in list :
#     print(f'employee {num}={i}')
#     num+=1
# list =[10,20,30,40,50,60,70]
# for i in list :
#     print (i)

# employee={
#     'name' : 'moustafa',
#     'age' : '25',
#     'salary' : '500000'
# }



# for key,value in employee.items() :
#     print(key,"------>", value)




# employees={
#     "employee 1": {
#                 'name' : 'moustafa',
#                 'age' : '25',
#                 'salary' : '900000'
#                 },
#      "employee 2":{
#                     'name' : 'hassan',
#                     'age' : '30',
#                     'salary' : '5020000'
#                 },
#     "employee 3":{
#                     'name' : 'moustafa',
#                     'age' : '29',
#                     'salary' : '3000'
#                 }
# }
# for mainkey,mainvalue in employees.items():
#     print(f"{mainkey}:")
    
#     for key,value in mainvalue.items():
#         print(f" {key}:{value}")



list = ['ramy ', 'mohamed ', 'hassn ', 'moustafa ']
# x = 0

# while x < len(list):
#     word = list[x]
#     g = 0
#     while g < len(word):
#         print(word[g])
#         g += 1
#     x += 1
    

x=0
while x<len(list):
    word= (list[x])
    x+=1
    y=0
    while y <len(word):
        print (word[y])
        y+=1
