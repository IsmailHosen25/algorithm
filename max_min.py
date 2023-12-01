import math

def fibonacci_search(func, a, b, epsilon=1e-5, max_iterations=100):
    fib = [0, 1]
    while (b - a) / epsilon > fib[-1]:
        fib.append(fib[-1] + fib[-2])
    x1 = a + (fib[-3] / fib[-1]) * (b - a)
    x2 = a + (fib[-2] / fib[-1]) * (b - a)

    for _ in range(2, max_iterations):
        if func(x1) < func(x2):
            b = x2
            x2 = x1
            x1 = a + (fib[-3] / fib[-1]) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + (fib[-2] / fib[-1]) * (b - a)

        fib = fib[:-2]

        if abs(b - a) < epsilon:
            return (a + b) / 2

    return (a + b) / 2
def objective_function(x):
    return x**2 + 4*x + 4  
a, b = -10, 10

result = fibonacci_search(objective_function, a, b)

print("Minimum value  =", result)
print("Objective function value at minimum:", objective_function(result))
