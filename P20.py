list1 = []
total=0
n=int(input("Enter the number of values to be added in the list : "))
for j in range(n):
    a=int(input("Enter a number for list : "))
    list1.append(a)
 
for i in range(0, len(list1)):
    total = total + list1[i]

print("Sum of all elements in given list: ", total)