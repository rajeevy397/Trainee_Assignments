def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

print(fibonacci_iterative(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
