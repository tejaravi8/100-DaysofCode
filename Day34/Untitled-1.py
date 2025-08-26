# from teja import mom

# c=mom()
# print(c.child2(2))

# Parent Class
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def show(self,n):
#         print(f"Name: {self.name}, Age: {self.age},{n}")

# # Child Class (inherits Person)
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)  # Reuse parent's constructor
#         self.student_id = student_id
    
#     def show_details(self):
#         super().show(1)  # Call parent method
#         print(f"Student ID: {self.student_id}")

# # Object
# s1 = Student("Teja", 22, "S101")
# s1.show_details()


# class human:
#     def sound(self):
#         name='teja'
        
# class dog(human):
#     def soun(self):
#         print('barks')
        
# class cat(human):
#     def soud(self):
#         return super().sound()
        
        
# a1=cat()
# print(a1.soud())


# class ind:
#     def sound(self):
#         print('india')
        
# class usa:
#     def sound(self):
#         print('america')
        
# def nation(country):
#     country.sound()

# a=ind()
# u=usa()
# nation(a)
# nation(u)

# Count how many times each character appears in a string (without Counter).


# Remove all duplicate characters from a string.

# str='stringin'
# new=''
# for i in str:
#     if i not in new:
#         new+=i
# print(new)
# Check if a string is an anagram of another.
# s1='listen'
# s2='silent'
# s2=list(s2)
# s1=list(s1)
# print(s1.sort()==s2.sort())
# Find the first non-repeating character in a string.

# Convert a string into title case (first letter capital for each word).
# t='hello raviteja hi'.split()
# new=''
# for i in t:
#     new+=i.upper()+" "
# print(new)
# 🔸 Numbers

# Check if a number is Armstrong or not.

# Find all prime numbers between two numbers.
# for i in range(2,10):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         print(i)
# Find the GCD (Greatest Common Divisor) of two numbers.

# Find the LCM (Least Common Multiple) of two numbers.

# Check if a number is a perfect number (sum of divisors = number).

# 🔸 Lists / Arrays

# Rotate a list left/right by k steps.
# a=[1,2,3,4,5]
# new=a[-2:]+a[:len(a)-2]
# print(new)
# Find the second smallest number in a list.

# Print all pairs in a list that sum up to a target number.
# a=[1,2,3,4,6,7,8,9,5]
# sum=9
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==9:
#             print((a[i],a[j]))
            
# Remove duplicates from a list without using set().

# Find the intersection of two lists without using set().

# 🔸 Patterns

# Print Pascal’s Triangle for n rows.

# Print a diamond pattern using *.

# Generate Floyd’s Triangle up to n rows.

# Print a hollow square pattern.

# Print this pattern:

# 1
# 12
# 123
# 1234
# 12345


# list=[2,5,7,9,6,4,5,1]
# f=s=float('inf')
# for i in list:
#     if i<f:
#         s=f
#         f=i
#     elif f<i<s:
#         s=i
# print(f,s)




# import copy

# list1 = [[1, 2], [3, 4]]
# # shallow = copy.copy(list1)

# # shallow[0][0] = 99   # Change nested list

# # print(list1)   # [[99, 2], [3, 4]]  → Affected!
# # print(shallow) # [[99, 2], [3, 4]]


# deep = copy.deepcopy(list1)

# deep[0][0] = 100
# print(list1)   # [[99, 2], [3, 4]] → Not affected
# print(deep)    # [[100, 2], [3, 4]]




# Write a program to flatten a nested list.
# new=[]

# def check(n):
#     for i in n:
#         if type(i)==list:
#             check(i)
#         else:
#             new.append(i)
# check(n=[1,[2,3],[4,[5,6]]])
# print(new)

# n=[1,[2,3],[4,[5,6]]]
# new=[]   
# for i in n:
#     if type(i)==list:
#         for j in i:
#             if type(j)==list:
#                 new.extend(j)
#             else:
#                 new.append(j)
#     else:
#         new.append(i)
# print(new)

# a=15
# b=30
# gcd=0
# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#         gcd=i
# print(gcd)

# print(type(lambda x: x*2))


# num=28
# def check(n):
    
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# if check(num):
#     print('near',num)
# else:
#     low=num-1
#     high=num+1
    
#     while True:
#         if low>1 and check(low):
#             print(low)
#             break
#         if high>1 and check(high):
#             print(high)
#             break
        
#         low-=1
#         high+=1

# num=8
# def check(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# if check(num):
#     print(num)
# else:
#     high=num+1
#     low=num-1
#     while True:
#         if high>1 and check(high) and check(low):
#             print(high,low)
#             break
#         high+=1
#         low+=1


num = int(input("Enter a number: "))

# check prime using loop
# def check_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# # if number itself prime
# print(check_prime(num))


num = int(input("Enter a number: "))

# # function to check prime
# def check_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# for i in range(2, num):
#     if check_prime(i) and check_prime(num - i):
#         print(num, "=", i, "+", (num - i))
#         break
# num = int(input("Enter a number: "))

# function to check prime
# def check_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# found = False
# for i in range(2, num):
#     if check_prime(i) and check_prime(num - i):
#         print(num, "=", i, "+", (num - i))
#         found = True

# if not found:
#     print(num, "cannot be expressed as the sum of two primes.")


def x():
    l=[1,2,3,4,5]
    max=-float("inf")
    for i in l:
        if i>max:
            max=i
    print(max)
x()
        





