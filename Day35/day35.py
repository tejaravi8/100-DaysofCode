# 🔹 Beginner Level

# Write a program to check if a given number is prime.

# Print all prime numbers between 1 and 50.

# Find the sum of all prime numbers between 1 and n.

# Count how many prime numbers are there between 1 and n.

# Input a number and print the next prime number after it.

# 🔹 Intermediate Level

# Input a number and print the nearest prime (smaller or larger).

# Input a number and print the two nearest primes if they are equally close.
# (Example: 12 → 11 and 13)

# Write a program to print the first 20 prime numbers.

# Write a program to print prime factors of a number.
# (Example: 28 → 2, 2, 7)

# Write a program to check if a number can be expressed as the sum of two primes.
# (Example: 34 → 3 + 31 or 5 + 29)

# 🔹 Advanced Thinking

# Find the largest prime number below 1000.

# Print all prime numbers in a given range [a, b].

# Find the difference between the largest and smallest prime in a given range.

# Given a list of numbers, print only the prime numbers from it.

# Print the first n twin primes (pairs of primes that differ by 2, like (3, 5), (5, 7)).


# l=[1,2,3,4,5,4]
# m=[1,2,9,0,5]
# new=[]

# for i in l:
#     if i in m:
#         new=new+[i]
#         print([i])
        
# print(new)


# num=6
# if 2>num:
#     print (False)
# for i in range(2,num):
#     if num%i==0:
#         break
# else:
#     high=num+1
#     low=num-1
#     while True:
#         for i in range(2,high):
#             if high%i==0:
#                 break
#         else:
#             print(high)
#             break
#         for i in range(2,low):
#             if low%i==0:
#                 break
#         else:
#             print(low)
#             break
            
            
        
    

# print(check(5))

# for i in range(1,20):
#     if check(i):
#         print(i)

# num=9
# high=num+1
# low=num-1
# if check(num):    #F
#     print(num)
# else:
#     while True:
#         if check(high):
#             print(high)
#             break
#         elif check(low):
#             print(low)
#             break
#         high+=1
#         low-=1


# num=[1,2,3]
# sum=''
# for i in num:
#     sum+=str(i)
# sum=int(sum)+1
# new=[]
# for i in str(sum):
#     new=new+[int(i)]
    
# print(new)



n=[1,2,3]
sum=0
for i in n:
    sum=i+sum*10
    
sum=sum+1
new=[]
while sum>0:
    r=sum%10
    new=[r]+new
    sum=sum//10
print(new)
    
    
# def check(num):
#     if 2>num:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True


# num=int(input('eneter number:'))
# high=num+1
# low=num-1
# count=0
# if check(num):
#         print(f'as well {num} also a prime')
# print()
# print('nearest two prime: ')
# while count<2:
#     if check(high) and count<2:
#         print(high)
#         count+=1
#     if check(low) and count<2:
#         print(low)
#         count+=1
#     high+=1
#     low-=1


# n=5
# count=0
# num=3
# while count<n:
#     if check(num) and check(num+2):
#         print(num,num+2)
#         count+=1
#     num+=1


# for i in range(1,21):
#     for j in range(i,21):
#         if check(i) and check(j):
#             if abs(i-j)==2:
#                 print(i,j)
                
# num=9
# high=num+1
# low=num-1
# if check(num):    #F
#     print(num)
# else:
#     count=0
#     while count<2:
#         if check(high):
#             print(high)
#             count+=1
#         if check(low):
#             count+=1
#             print(low)
#         high+=1
#         low-=1
# for i in l:
#     if check(i):
#         if low is None:
#             low=i
#             high=i
#         else:
#             if i<low:
#                 low=i
#             if i>high:
#                 high=i
# print(high-low)


# a=10
# b=30
# new=[]
# for i in range(a,b+1):
#     if check(i):
#         new=new+[i]

# print(abs(new[0]-new[-1]))
# a=10
# b=30
# small=None
# Large=None
# for i in range(a,b+1):
#     if check(i):
#         if small is None:
#             small=i
#         Large=i
# print(Large-small)




# num=int(input('enter:'))
# count=0
# high=1
# while count<num:
#     if check(high):
#         print(high)
#         count+=1
#     high+=1

# ascii




# Write a program to check if a number can be expressed as the sum of two primes.
# (Example: 34 → 3 + 31 or 5 + 29)

# num=34
# found=True
# i=1
# while found:
# num=None
# i=1000
# while i>1:
#     if check(i) and num == None:
#         num=i
#     i-=1
# print(num)
        



# count=0
# i=2
# while i>1:
#     if check(i):
#         count+=1
#         print(i)
#     if count==20:
#         break
#     i+=1
    
# for i in range(1,100):
#     if check(i):
#         n.append(i)
#     if len(n)==20:
#         break
# print(n)


def palindrome(name):
    if str(name)==str(name)[::-1] :
        return True
    else:
        return False
    

    
# n=[]
# for i in range(2,100):
#     if check(i) or palindrome(i):
#         n.append(int(i))
        
# print(n)


# 🔹 Prime Number Logic

# Print all prime numbers between 1 and n.

# Print the first n prime numbers.

# Find the sum of the first n prime numbers.

# Print the largest prime smaller than a given number n.

# Print the first n twin primes (we solved this).

# 🔹 Number Patterns & Properties

# Check if a number is Armstrong (153 = 1³+5³+3³).

# Check if a number is a Strong number (145 = 1!+4!+5!).

# Check if a number is a Palindrome (same forwards & backwards).

# Check if a number is an Automorphic number (its square ends with itself, e.g. 25² = 625).

# Check if a number is a Harshad number (divisible by sum of its digits).


num=11
n=num
s=0
while num>0:
    s=s+num%10
    num//=10

if n%s==0:
    print(True)
else:
    print(False)
# 🔹 Series & Sequences

# Generate the first n Fibonacci numbers.

# Print all Fibonacci primes up to n.

# def fibo(n):
#     a,b=0,1
#     for _ in range(1,n+1):
#         a,b=b,a+b
#         if check(a) and a<=n:
#             print(a)
#         if a==n:
#             break
# fibo(233)
        

# Print all numbers up to n that are both prime and palindrome.

# Print all numbers up to n that are both Armstrong and palindrome.

def arm(num):
    n=num
    sum=0
    while n>0:
        sum=(n%10)**3 + sum
        n//=10
    if sum==num:
        return True
    else:
        return False

# pal=[]
# ar=[]
# for i in range(100,1000):
#     if palindrome(i):
#         pal.append(i)
#     if arm(i):
#         ar.append(i)
    
# print(pal,'arm:',ar)
        
# n=1000
# for i in range(100,n+1):
#     if 
    
# Generate the first n factorial numbers.

# n=5

# for i in range(1,n+1):
#     fact=1
#     for j in range(1,i+1):
#         fact*=j
#     print(fact,i)
        

# 🔹 Logical Challenges

# Print all numbers up to n that have exactly 3 divisors.
# for i in range(1,100):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)
            

# Print the prime gap (difference between consecutive primes) up to n.
# high=0
# low=0
# for i in range(2,100):
#     if check(i) and i>high:
#         low=high
#         high=i
#         print('gap:',high-low,i)
        


# Check if a number can be written as the sum of two squares.

# num=25
# for i in range(1,num):
#     for j in range(i,num):
#         if (i**2)+(j**2)==num:
#             print(i,j)
#             print(f"{i**2}+{j**2} = {num}")


# Find the nth prime number.

# num=0
# i=1
# n=[]
# while i>0:
#     if check(i):
#         num+=1
#         n.append(i)
#     if num==8:
#         print(i)
#         print(n)
#         break
#     i+=1
        

# Print all perfect numbers up to n (sum of divisors = number).