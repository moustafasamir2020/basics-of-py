# str------------->
# name= 'moustafa samir'
# print (type (name) )
# name .capitalize()
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# name2=input("enter your name:").strip()
# name2=input("enter your name:").split('m')

# print (name2)
# name2=input("enter your name:").split('m')

# name2=input("enter your name:").count()
# name="moustafa samir abdelghafar"
# print(name.count('o'))
# print(name.count('u'))
# print(name.index('a'))
# print(name.startswith('m'))
# print(len(name))
# print(name[0:10])
# print(name[15:])
# print(name[0:14:2])
# print(name[::-1])
# list------------->
# name=['moustafa','samir','ahmed','omnia','lobna']
# age=[1,2,3,4,5,5,6]
# print(len(name))
# print(type(name))
# name.append('hesham')
# name.insert(2,'hatem')
# name.append(age)
# print (name.count("lobna"))
# name.pop(2)
# print(name)
# name.remove("moustafa")
# name.clear()
# name.extend(age)
# name[1]="mohamed"
# print(name)
# # dictionary-------------------->
employee={
    'name':'omar',
    'age':'26',
    'station':"acount",
    
}




# e= employee.copy()
# employee.pop('age')
# print(e)
# print(employee)
# print (employee.keys())
# print (employee.values())
# print (employee.items())
employee.update({'name':'moustafa'})
# print (employee)
# Name={
#     'employee1':{'name':'omar',
#     'age':'26',
#     'station':"acount"},

#     'employee2':{'name':'omar',
#     'age':'26',
#     'station':"acount"},

#     'employee3':{'name':'omar',
#     'age':'26',
#     'station':"acount"},
# }
# Name['employee1']={'name':'moustafa',
#     'age':'26',
#     'station':"acount"}





word = "moustafa"
index = 0
while index < len(word):
    print(word[index])
    index += 1
