list1 = []
total=0
n=int(input("Enter the number of values to be added in the list : "))
for j in range(n):
    a=int(input("Enter a number for list : "))
    list1.append(a)
max=max(list1)
min=min(list1)

print(f'The maximum value in the list is {max}')
print(f'The minimum value in the list is {min}')