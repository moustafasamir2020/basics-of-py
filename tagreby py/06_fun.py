# def sum_two(x,y):
#     print(x+y)

# def min_two(x,y):
#     print ( x-y)

# def mul_two(x,y):
#     print ( x*y)

# def div(x,y):
#     print ( x/y)



# while True:
        
#         choose= input ('press k to continue or s to stop :')
#         if choose== 'k':
#             num1=float(input('enter first number :'))
#             num2=float(input('enter second number :'))
#             ope=input('enter your ope + - * /   :')
#             if ope == '+' :
#                 sum_two (num1,num2)
#             elif ope =='-':
#                 min_two (num1,num2)
#             elif ope =='*':
#                 mul_two (num1,num2)
#             elif ope == '/':
#                 div (num1,num2)
#         elif choose == 's':
#                 break   


# def sum (num1,num2):
#     return(num1+num2)


# print (sum(2,4))


# def max (num1,num2,num3):
#     if num1>num2 and num1>num3 :
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
    

# print (max(10,50,30))



# employee={
#     'name' : 'moustafa',
#     'age' : '25',
#     'salary' : '500000'
# }


# print (employee.get('hab', 'not do'))
# x=1
# while x<=10:
#     x+=1
#     if x==5 :
#         continue
#     if x==6 :
#         break
#     print(x)
# else:
#     print('end to' )


# print ('end')


# n=23

# if n % 2 != 0 or 5 < n < 21 :
#     print("Weird")
# else:
#     print("Not Weird")



if __name__ == '__main__':
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name,score])
    findScore = [x[1] for x in lst]
    sortScore = sorted(set(findScore))
    findName = sorted([y[0] for y in lst if(sortScore[1] == y[1])])
    for z in findName:
        print(z)

