import math
# Probability tools
def permut(a,b=1):

  if a>=b and a>=0 and b>=0:
    return (math.factorial(a)//(math.factorial(a-b)))
  elif a<b:
    return "Error"

def comb(a,b=1):
    if a>=b and a>=0 and b>=0:
      return (math.factorial(a)//(math.factorial(a-b)*math.factorial(b)))
    elif a<b:
      return "error"

def prob(sample_size,favaourable_outcomes_number=1):
  if sample_size!=0:
    return favaourable_outcomes_number/sample_size
  else:
    return "Sample size can't be 0"

# Geometry Tools
def area_of_circle(radius):
  if radius >0:
    return math.pi*radius**2
  else:
    return "Radius can't be negative"

def area_of_triangle(a,b,c):
  if a>0 and b>0 and c>0:
    s = (a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))
  else:
    return "Error. sdes can't be negative or 0"

def volume_of_sphere(radius):
  if radius>0:
    return 4/3*math.pi*radius**3
  else:
    return "Error. Radius can't be negative"

def area_of_regular_ngon(n,r):
  if not isinstance(n,int) or r<=0:
    return "Error. Invalid number of sides or non-positive radius"
  else:
    return (1/2*n*r**2*math.sin((2*math.pi)/n))

# Number theory
def gcf(a,b):
  return math.gcd(a,b)
def lcm(a,b):
  return math.lcm(a,b)
def is_even(a):
  return True if a%2==0 else False
def factorial(a):
  if a==0 or a==1:
    return 1
  else:
    return a*factorial(a-1)
# Percentages and Interest
def percent(part,whole):
  if whole!=0:
    return part/whole*100
  else:
    return "error"
def simple_interest(P,r,t):
  return (P+P*r*t)
def cpd_interest(P,r,t,n=1):
  return (P*(1+r/n)**(n*t))

# Written  by Dagaa Addisu on Feb 22 
