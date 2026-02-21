# Math  Functions 
# Written by Dagaga A. Feb 20
import math
def add(a,b):
    return a+b
def divide(a,b):
    if b!=0:
        return f"{a/b:.2f}"
    else:
        return "Division by zero"
        
def sqrt(a):
    return f"{(a)**(1/2):.2f}"
def mod(a,b):
    return a%b
def comb(a,b):
    if a>b:
        return (math.factorial(a))/(math.factorial(a-b)*math.factorial(b))
    else:
        return "something went wrong"
def permut(a,b):
    if a>b:
        return (math.factorial(a))/math.factorial(a-b)

# print(add(3,4))
# print(divide(3,4))
# print(sqrt(4))
# print(mod(10,3))
# print(comb(4,3))
# print(permut(5,4))
