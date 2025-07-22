# 4.	Generate a tuple of prime numbers between 10 to 50 using comprehension.

primes = tuple(x for x in range(10, 51) if all(x % i != 0 for i in range(2, int(x**0.5) + 1)))
print(primes)

# for i in range(10,51):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print("prime")