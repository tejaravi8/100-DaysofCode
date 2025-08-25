# Python Mock Test – 30 Problems
# Section A – Easy (10 Problems)

# (Approx. 20 mins)

# Write a program to print the first 10 natural numbers using a loop.
# n=1
# while n<=10:
#     print(n)
#     n+=1

# # Write a program to find the sum of all numbers in a list.
# lis=[1,2,3,4,5,6,7]
# sum=0
# for i in lis:
#     sum+=i
# print(sum)

# # Given a string, count how many vowels it contains.
# str='Given a string'
# count=0
# for i in str:
#     if i.lower() in 'aeiou':
#         count+=1
# print(count)
        
# Create a dictionary from two lists: keys = ['a','b','c'], values = [1,2,3].
# keys = ['a','b','c']
# values = [1,2,3]
# dict={}
# for i,j in zip(keys,values):
#     dict[i]=j
# print(dict)

    
# Write a program to check if a given number is even or odd.
# num=8
# if num%2==0:
#     print('even')
# else:
#     print('odd')

# Write a program to copy contents from one text file to another.
# a=open('teja.txt','w')
# x=a.write('tejaa')

# with open('ravi.txt','r') as p:
#     a=p.read()
#     with open('pablo.txt','w') as s:
#         s.write(a)
        

# Print all elements of a list along with their index using enumerate.
# list=[1,2,3,4,5,6,7,8,9,10]
# for index,j in enumerate(list,start=0):
#     print(index,j)
    
# Write a program to read a file and count how many lines it has.
# with open('pablo.txt','r') as s:
#     a=s.readlines()
#     print(len(a))

# Write a program to find the maximum number in a list without using max().
# list=[1,3,8,2,4,9,6]
# first=0
# for i in list:
#     if i>first:
#         first=i
# print(first)
# Write a program to merge two lists into a dictionary (list1 → keys, list2 → values).
# keys = ['a','b','c']
# values = [1,2,3]
# dict={}
# for i in range(len(values)):
#     dict[keys[i]]=values[i]
# print(dict)    
# dict={}
# for i,j in zip(keys,values):
#     dict[i]=j
# print(dict)
# Section B – Medium (12 Problems)

# (Approx. 40 mins)

# Write a program to reverse a string without using slicing ([::-1]).

# str='programming'
# new=''
# for i in str:
#     new=i+new
# print(new)

# Write a program to count the frequency of each word in a file.
# freq={}
# with open('pablo.txt','r') as s:
#     a=s.read().split()
#     for i in a:
#         if i not in freq:
#             freq[i]=1
#         else:
#             freq[i]+=1
# print(freq)

# # str='programming'
# # freq={}
# # for i in str:
# #     if i in freq:
# #         freq[i]+=1
# #     else:
# #         freq[i]=1
# # print(freq)    
    
# Write a program to remove duplicates from a list.
# list=[1,2,3,4,5,1,2]
# new=[]
# for i in list:
#     if i not in new:
#         new.append(i)
# print(new)
# Given a dictionary, find the key with the largest value.
# dict={
#     'ravi':1,
#     'teja':2,
#     'pablo':3,
#     'durva':4
# }
# key=''
# value=0
# for i,j in dict.items():
#     if j>value:
#         key=i
#         # value=j
# print(key)
        
# Write a program to check if a given substring exists in a string.
# str='raviteja'
# sub='tej'
# if sub in str:
#     print('exist')
# else:
#     print('not found')
# # Write a program to flatten a nested list.
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

# Write a program to count how many times a specific word appears in a file (case-insensitive).
# dict={}
# with open('pablo.txt','r') as p:
#     a=p.read().split()
#     for i in a:
#         if i in dict:
#             dict[i]+=1
#         else:
#             dict[i]=1
# print(dict)
    
# Write a program to print all prime numbers between 1 and 50.
# for i in range(2,51):
#     count=0
#     for j in range(2,i):
#         if i%j ==0:
#             count+=1
#     if count==0:
#         print(i)
# num=1
# while num<=50:
#     for i in range(2,num):
#         if num%i==0:
#             break
#     else:
#         print(num)
#     num+=1
               
                  
# Given a list of numbers, print the second largest number.
# list=[1,2,3,9,6,4,7,10,5]
# first=second=0
# for i in list:
#     if i>first:
#         second=first
#         first=i
#     elif first>i>second:
#         second=i
# print(second,first)
        
# Write a program to replace all occurrences of a given word in a file with another word.
# new=[]
# with open('pablo.txt','r') as s:
#     a=s.read().split()
#     for i in a:
#         if i=='hello':
#             new.append('hell')
#         else:
#             new.append(i)
            
# data='teja is good boy'
# new=data.replace('teja','pablo')
# print(new)
# print(new)
# Write a program to find the sum of all even numbers in a given range. 
# sum=0
# for i in range(1,51):
#     # if i%2==0:
#     sum+=i
# print(sum)
        
# Write a program to print only lines 5 to 10 from a file.............................................

# with open('teja.txt','r') as p:
#     a=p.readlines()
#     for i in range(3):
#         print(a[i], i+1)
        
# Section C – Hard (8 Problems)

# (Approx. 30 mins)

# Write a program to read a CSV file and print only the first column values.........................................................

# Write a program to check if two strings are anagrams of each other.
# str1='silent'
# str2='listen'

# if sorted(str1)==sorted(str2):
#     print('anagram')
# else:
#     print('not an anagram')
# Write a program to merge the contents of two files into a third file without duplicates.
# with open('pablo.txt','r') as p:
#     a=p.read()
#     with open('ravi.txt','r') as r:
#         b=r.read()
#         with open('new.txt','a') as n:
#             n.write(a)
#             n.write(b)
# Write a program to sort a dictionary by its values in descending order.      ..........................................................
# scores = {"Teja": 90, "Ravi": 75, "Kiran": 95, "Anil": 80}

# # Convert dictionary into list of tuples
# items = list(scores.items())   # [('Teja', 90), ('Ravi', 75), ('Kiran', 95), ('Anil', 80)]

# # Sort by value (2nd element) using index
# for i in range(len(items)):
#     for j in range(i+1, len(items)):
#         if items[i][1] < items[j][1]:   # compare values
#             items[i], items[j] = items[j], items[i]   # swap

# # Convert back to dictionary
# sorted_dict = dict(items)
# print(sorted_dict)

# Write a program to read a file and print only the lines that do not contain a given word.
# with open('teja.txt','r') as p:
#     a=p.read().splitlines()
#     for i in a:
#         if 'goodbye' not in i:
#             print(i)
            
            # [line is 1 , line]
# Write a program to generate Fibonacci numbers up to n using recursion.
# n=10
# a,b=0,1
# for i in range(n):
#     print(a)
#     a,b=b,a+b
# Write a program to find the longest word in a file.
# max=''
# with open('pablo.txt','r') as p:
#     a=p.read().split()
#     for i in a:
#         if len(i)>len(max):
#             max=i
# print(max)
    
# Write a program to read a nested dictionary and print all keys and values in a structured format.

# dict={'teja':{'t':1}}

# for i,j in dict.items():
#     for k,l in j.items():
#         print(l)


# students = {
#     "student1": {"name": "Teja", "age": 22, "marks": 90},
#     "student2": {"name": "Ravi", "age": 23, "marks": 85}
# }

# for i,j in students.items():
#     print(f"{i}:")
#     for k,l in j.items():
#         print(f"        {k}:{l}")
#     print()
# students = {
#     "student1": {"name": "Teja", "age": 22, "marks": 90},
#     "student2": {"name": "Ravi", "age": 23, "marks": 85}
# }

# for outer_key, inner_dict in students.items():   # loop through main dictionary
#     print(outer_key + ":")                       # print student1, student2
#     for inner_key, value in inner_dict.items():  # loop inside dictionary
#         print("   ", inner_key, ":", value)      # structured format
#     print()



# scores = {"Teja": 90, "Ravi": 75, "Kiran": 95, "Anil": 80}

# scores=list(scores.items())   # [ ('teja',90),('ravi',75),..]
# for i in range(len(scores)):
#     for j in range(i+1,len(scores)):
#         if scores[i][1]>scores[j][1]:
#             scores[i],scores[j]=scores[j],scores[i]
#         else:
#             scores[i],scores[j]=scores[i],scores[j]
# print(scores)



# num=120  # 1,3,5,15
# num2=60  # 1,2,3,5,6,10,15,30

# gcd=1

# for i in range(1,min(num,num2)+1):
#     if num%i==0 and num2%i==0:
#         gcd=i
# print(gcd)

# def gcd(a,b):
#     gcd=1
#     for i in range(1,min(a,b)+1):
#         if a%i==0 and b%i==0:
#             gcd=i
#     print(gcd)
# gcd(120,60)


# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)

# print(gcd(15,30))

# Create a function that accepts a list of integers and returns a new list with only prime numbers.

# def check(n):
#     new=[]
#     for i in n:
#         if i==1:
#             continue
#         for j in range(2,i):
#             if i%j==0 :
#                 break
#         else:
#             new.append(i)
#     return new
        
    
# print(check(n=[1,2,3,4,5,6,7,8,9,10,11,12,13]))


# student = {"name": "Teja", "age": 22}

# # print(student["nam"])      # Teja
# print(student.get("nam"))  # Teja



# with open('teja.txt','a') as p:
#     p.write('hello every one')
    
    
# lines
# with open('teja.txt','r') as p:
#     a=p.readlines()
#     print(len(a))

# most repeated
# dict={}
# max=0
# key=''
# with open('teja.txt','r') as p:
#     a=p.read().split()
#     for i in a:
#         if i not in dict:
#             dict[i]=1
#         else:
#             dict[i]+=1
# for i,j in dict.items():
#     if len(i)>len(key):
#         key=i
# print(key)
# freq



# file delete exist
# file



# list=[1,4,5,7,8,2,5]

# first=sec=thr=0
# for i in list:
#     if i>first:
#         thr=sec
#         sec=first
#         first=i
#     elif first>i>sec:
#         sec=i
#     elif sec>i>thr:
#         thr=i
# print(first,sec,thr)



# flatten nested , file handling,gcd, binary , recursion

# teja=lambda x: x*2
# print(teja(2))

# lambda arguments:expression

# nums = [1,2,3,4,5]
# squares=list(map(lambda x:x**2,nums))
# print(squares)

# nums=[1,2,3,4,5,6,7,8,9]
# filtered=list(filter(lambda x :x%2==0,nums))
# print(filtered)

# students = [("Teja", 22), ("Ravi", 20), ("Kiran", 25)]
# sorted_students=(students,key=lambda x:x[1])
# print(sorted_students)

# words = ["apple", "banana", "cherry", "fig"]
# print(sorted(words, key=lambda w: len(w)))

# a='i'
# key=lambda x : len(x)
# sorted(),max(),min(),abs(),a.sort()

# from functools import reduce

# nums = [1, 2, 3, 4, 5]
# j=reduce(lambda a,b:a+b,nums)
# print(j)

# nums = [1, 2, 3, 4]
# str_list = list(map(lambda x: x%2, nums))
# print(str_list)

# students = [
#     {"name": "Teja", "marks": 85},
#     {"name": "Ravi", "marks": 92},
#     {"name": "Kiran", "marks": 78}
# ]

# top=max(students,key=lambda x:x['marks'])
# print(top)

# is_even = lambda x: x % 2 == 0
# print(is_even(6))   # True
# print(is_even(7))   # False

# lambda without variable assignment
# print((lambda x,y:x+y)(1,2))

# from functools import reduce
# nums=[1,2]
# a=reduce(lambda x,y:x+y,nums)
# print(a)

# nums = [5, 8, 3, 10, 2]
# n=min(nums,key=lambda x:x)
# print(n)

# from functools import reduce
# nums=[1,2,3,2,5]
# # m=reduce(lambda a,b:a*b,nums)
# # print(m)

# result=reduce(lambda a,b: b if a>b else a,nums)
# print(result)

# a=bin(7)
# print(a)
# num=6
# binary=''
# while num>0:
#     rem=num%2
#     binary=str(rem)+binary
#     num=num//2
# print(binary)

# to_binary = lambda n: bin(n)
# print(to_binary(10))


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else: 
#         return n * factorial(n-1)

# print(factorial(3))  # 120

# def fib(n):
#     if n <= 1:  # base case
#         return n
#     return fib(n-1) + fib(n-2)  # recursive case

# print(fib(6))  # 8


# a='teja'
# print(a.capitalize())

# table = [[i*j for j in range(1, 11)] for i in range(1, 11)]
# print(table,)

# matrix = [[1, 2, 3], [4, 5, [6,8]], [7, 8, 9]]
# flatten = [num for row in matrix for num in row]
# print(flatten)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]



