n=int(input("Enter the number of times fibonacci sequence should be printed : "))
a=0
b=1
for i in range(n):
    
    print(a)
    a,b=b,a+b
