list1 = []
n=int(input("Enter the number of values to be added in the list : "))
for j in range(n):
    a=input("Enter a element for list : ")
    list1.append(a)

x=input("Enter the element you wish to find the occurance of : ")
y=list1.count(x)
print(f"The element {x} has occured {y} times")