def sum_two(x,y):
    print(x+y)

def min_two(x,y):
    print ( x-y)

def mul_two(x,y):
    print ( x*y)

def div(x,y):
    print ( x/y)



while True:
        
        choose= input('press k to continue or s to stop :')
        if choose== 'k':
            num1=float(input('enter first number :'))
            num2=float(input('enter second number :'))
            ope=input('enter your ope + - * /   :')
            if ope == '+' :
                sum_two (num1,num2)
            elif ope =='-':
                min_two (num1,num2)
            elif ope =='*':
                mul_two (num1,num2)
            elif ope == '/':
                div (num1,num2)

        elif choose == 's':
                break   






