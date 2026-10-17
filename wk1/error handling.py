#this is just a simple calculator using function

#define addition function

def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiply(*args):
    ans = 1

    for i in args:
        ans = ans * i

    return ans

def divide(a,b):
    try:
        a//b
    except ZeroDivisionError as e:
        print("you can't divide by zero")


equation = input("Your first number ")
times = "*"
division = "/"
subtract = "-"
plus = "+"
if times in equation:
    operand = times
elif division in equation:
    operand = division
elif subtract in equation:
    operand = subtract
elif plus in equation:
    operand = plus

equation=equation.split(operand)

a = int(equation[0])
b = int(equation[1])

if plus == operand:
    ans = add(a, b)
    print(ans)
elif subtract == operand:
    ans = minus(a, b)
    print(ans)
elif times == operand:
    numbers = [int(num) for num in equation]
    ans = multiply(*numbers)
    print(ans)
elif division == operand:
    ans = divide(a, b)
    print(ans)



