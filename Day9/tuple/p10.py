# Generate a tuple of prime numbers between 10 to 50 using comprehension. 

primes=tuple(i for i in range(10, 51) if all(i % j != 0 for j in range(2, i)))  #(2, int(i**0.5) + 1)
print(primes)