# # 5. Lists & Dictionaries
# # Write a program to find the largest number in a list.

# # numbers=[1,2,3,4,9,8,12,6,5,10,6]
# # maximum=numbers[0]
# # for i in numbers:
# #     if i>maximum:
# #         maximum=i
# # print(maximum)
    

# # Write a program to find the second largest number in a list.
# # numbers=[1,2,3,4,9,8,12,6,5,10,6]
# # first=second=numbers[0]

# # for i in numbers:
# #     if i>first:
# #         second=first
# #         first=i
# #     elif first>i>second:
# #         second=i
# # print(first,second)

# # Write a program to remove duplicates from a list.
# # numbers=[1,2,3,4,9,8,12,6,5,10,6]
# # number=[]
# # for i in numbers:
# #     if i not in number:
# #         number.append(i)
# # print(number)


# # Write a program to merge two lists into a dictionary (keys from first, values from second).

# # name=['teja','pablo','durvasulu','charan']
# # roll=[1,2,3,4]
# # new={}
# # for i,j in zip(name,roll):
# #     new[i]=j
# # print(new)

# # Write a program to find the sum of all items in a dictionary.
# # d={'teja': 1, 'pablo': 2, 'durvasulu': 3, 'charan': 4}
# # sum=0
# # for i,j in d.items():
# #     sum+=1
# # print(sum)

# # Write a program to sort a list without using built-in functions.
# # numbers=[1,2,3,4,9,8,12,6,5,10,6]

# # for i in range(len(numbers)):
# #     for j in range(i+1,len(numbers)):
# #         if numbers[i]<numbers[j]:
# #             numbers[i],numbers[j]=numbers[i],numbers[j]
# #         else:
# #             numbers[i],numbers[j]=numbers[j],numbers[i]
# # print(numbers)
        
# # Write a program to count how many times each element appears in a list.
# # numbers=[1,2,3,4,5,3,4,6,1,1,7]
# # f={}
# # for i in numbers:
# #     if i in f:
# #         f[i]+=1
# #     else:
# #         f[i]=1
# # print(f)

# # Write a program to check if a key exists in a dictionary.
# # b={1: 3, 2: 1, 3: 2, 4: 2, 'teja': 1, 6: 1, 7: 1}
# # for i in b:
# #     if i=='teja':
# #         print(True)

# # Write a program to find the key with the maximum value in a dictionary.
# # b={1: 3, 2: 1, 3: 2, 4: 2, 'teja': 7, 6: 1, 7: 1}
# # max=0
# # key=None
# # for j,i in b.items():
# #     if i>max:
# #         max=i
# #         key=j
# # print(key)

# # Write a program to update a dictionary with another dictionary’s values.
# # b={1: 3, 2: 1, 3: 2, 4: 2, 'teja': 7, 6: 1, 7: 1}

# # b['teja']=6

# # print(b)


# # 6. File Handling
# # Write a program to create a text file and write some data to it.

file=open('teja.txt','r')
a=file.read()
print(a)
    
# # Write a program to read a text file and display its contents.

# # Write a program to count the number of lines in a file.

# # Write a program to copy the contents of one file to another.

# # Write a program to count the number of words in a file.
file=open('teja.txt','r')
a=file.read()
print(len(a))


# 7. Common Interview Puzzles
# Write a program to swap two numbers without using a third variable.
# a=5
# b=4
# a,b=b,a
# print(a,b)
# Write a program to check whether a number is an Armstrong number.

# num=153
# a=num
# sum=0
# while num>0:
#     sum+=(num%10)**3
#     num=num//10
# if sum==a:
#     print('armstrong')
# else:
#     print('not')

# Write a program to find the GCD of two numbers.

# num1=45
# num2=30
# num1_count=0
# for i in range(1,num1):
#     if num1%i==0:
#         if num1_count<i:
#             num1_count=i
# print(num1_count)
        
# Write a program to check if a number is a palindrome.

# num=12321
# a=num
# rev=0
# while num>0:
#     rev=num%10+rev*10
#     num=num//10
# if a==rev:
#     print('palindrome')
# else:
#     print('not a palindrome')
    
    

# Write a program to print all prime numbers between 1 and 100.
# n=100
# for i in range(1,n+1):
#     if i!=1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# Write a program to remove duplicates from a string.

# str='raviteja'
# new=''
# for i in str:
#     if i not in new:
#         new+=i
# print(new)

# Write a program to rotate a list n times to the right.

# n=2
# rotate=[1, 2, 3, 4, 5, 6]
# new=rotate[-n:]+rotate[:-n]
# print(new)


# Write a program to flatten a nested list.

# flat = []

# def flatten(lst):
#     for i in lst:
#         if isinstance(i, list):  # if element is a list
#             flatten(i)  # call the same function again (recursion)
#         else:
#             flat.append(i)  # if it's not a list, store it
# flatten([1, [2, 3], [4, [5, 6]]])
# print(flat)  # [1, 2, 3, 4, 5, 6]


# b=[]
# for i in a:
#     if type(i)==list:
#         # b.extend(i)
#         for j in i:
#             if type(j)==list:
#                 b.extend(j)
#     else:
#         b.append(i)
# print(b)

# Write a program to generate random numbers between 1 and 10.

# import random
# count=0
# while True:
#     a=random.randint(1,10)
#     print(a)
    # if a==5:
    #     print('itercount:',count)
    #     break
    # else:
    #     count+=1
    

# Write a program to find all the factors of a number.

# num=12
# for i in range(1,num):
#     if num%i==0:
#         print(i)
        
# i=1  
# num=12   
# while i<num:
#     if num%i==0:
#         print(i)
#     i+=1
    
        