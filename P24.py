def sum(num1,num2):
    s=num1+num2
    print(f"The sum of {num1} and {num2} is : {s}")

def diff(num3,num4):
    d= num3-num4
    print(f"The difference of {num3} and {num4} is : {d}")

def mult(num5,num6):
    m= num5*num6
    print(f"The product of {num5} and {num4} is : {m}")

def div(num7,num8):
    if num8>0:
        quo= num7/num8
        print(f"The difference of {num7} and {num8} is : {quo}")
    elif num8==0:
        print('The second number cannot be zero')


a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
o=input("Enter what operation u wish to apply (+,-,*,/) : ")
if o == '+':
    sum(a,b)
elif o == '-':
    diff(a,b)
elif o == '*':
    mult(a,b)
elif o == '/':
    div(a,b)
else:
    print('Enter a valid operation!')
