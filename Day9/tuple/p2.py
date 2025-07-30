# Find factors of 10 number using tuple comprehension?

factors = tuple([i for i in range(1, n+1) if n % i == 0] for n in range(1, 11))
print(factors)