str1= input(" Enter first string : ")
str2= input(" Enter second string : ")

dict1 = {}

for i in str1:
   
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

dict2 = {}

for i in str2:
   
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 1

if dict1==dict2:
    print("the given strings are amalgams")
else:
    print("the strings are not amalgams")