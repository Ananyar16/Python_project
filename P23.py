temp= float(input("Enter temperaure value : "))
unit= input("Enter the unit of the temperature value (C/F) : ")
unit=unit.upper()
if unit=='C':
    fr = (temp * 1.8) + 32
    print(f"Converting the temperature into farhenheit: {fr} F ")
elif unit == "F":
    cl= (temp-32)/1.8
    print(f"Converting the temperature to celcius: {cl} C")
