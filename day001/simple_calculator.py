# Calculator - Feb 15 by Dagaga A.

a = float(input("> a: "))
op = input("> Enter a valid operator: +,-,/,* ")
b = float(input("> b: "))

if op=="+":
    print(f"{a}+{b}=",a+b)
elif op=="-":
    print(f"{a}-{b}=",a-b)
elif op=="*":
    print(f"{a}*{b}=",a*b)
elif op=="/":
    if b!=0:
        print(f"{a}/{b}=",a/b)
    else:
        print("Sorry, can't devide by zero ")
else:
    print("Invalid or unrecognized symbol! Try using +,-,* or / ")

"""
> a: 30
> Enter a valid operator: +,-,/,* +
> b: 37
30.0+37.0= 67.0
"""
