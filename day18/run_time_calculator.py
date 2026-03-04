from functools import wraps
import time
def timer(func):
  @wraps(func)
  def wrapper(*args,**kwargs):
    start = time.time()
    value = func(*args,**kwargs)
    end = time.time()
    print(f"Runtime: {end-start:.2f}")
    return value
  return wrapper

@timer
def looper(n):
  for i in range(1,n+1):
    print(i**2)
looper(30)
# Problem name was: Create @timer decorator.
# written by dagaga addisu on March 4
