# Calculator with error handling
try:
    a = float(input("num 1... "))
    b = float(input("num 2... "))
    operator = input("+,-,*,/ ")
    if operator not in ['+','-','*','/']:
        print("Please. Choose only the given operators: +,-,*,/")
    else:
        if operator=='+':
            print(a+b)
        elif operator=='-':
            print(a-b)
        elif operator=='*':
            print(a*b)
        elif operator=='/':
            try:
                print(a/b)
            except ZeroDivisionError:
                print("can't divide by 0")
except ValueError:
    print("Please enter valid arabic numerals!")
# Written by Dagaga A. Feb 25
