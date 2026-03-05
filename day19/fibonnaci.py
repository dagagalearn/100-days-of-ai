def fibonacci(n):
    if n <= 0:
        print("n can't be negative or 0")
        return
    a, b = 1, 1

    for _ in range(n):
        yield a
        a, b = b, a + b
        
for num in fibonacci(4):
	print(num)
