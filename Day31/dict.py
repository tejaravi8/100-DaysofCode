# Given a list of student names and scores, create a dictionary and find the top 3 scorers.

# student_scores ={
#     'ravi': 80,
#     'kumar': 70,
#     'kiran': 60,
#     'suresh': 50,
#     'ramesh': 40
# }

# list=list(student_scores.items())

# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if list[i][1]<list[j][1]:
#             list[i],list[j]=list[j],list[i]
#         else:
#             list[i],list[j]=list[i],list[j]
            
# # print(list)
# for i in range(3):
#     print(list[i])


# Convert a nested dictionary into a flattened dictionary. Example:

# {"a": {"b": 1, "c": 2}, "d": 3} → {"a.b": 1, "a.c": 2, "d": 3}

# Write a program to group words by their first letter using a dictionary.
# Example: ["apple", "banana", "apricot", "berry"] → {"a": ["apple","apricot"], "b": ["banana","berry"]}

# fruits=["apple", "banana", "apricot", "berry","avocado"]
# dict={}

# for i in fruits:
#     if i[0] not in dict:
#         dict[i[0]]=[i]
#         print(dict)
#     else:
#         dict[i[0]].append(i)
# print(dict)
    

# Use list comprehension to generate all perfect squares less than 500.
# new=[i for i in range(1,501) if i=((i**2)**0.5)]

# new=[i**2 for i in range(1,500) if i**2<500]
# print(new)
# for i in range(1,num+1):
#     if i**2<num:
#         print(i**2)

# Use dictionary comprehension to count vowels in a string.

# text='hello world'
# vowels='aeiou'
# count=0
# dict={i:text.count(i) for i in vowels if i in text}
# # for i in text:
# #     if i in vowels:
# #         count+=1
# #         if i not in dict:
# #             dict[i]=1
# #         else:
# #             dict[i]+=1
        
# print(dict)
# p=0
# for i in text:
#     p+=vowels.count(i)
# print(p)

# Write a program to find the second most frequent character in a string.

# str='frequent character'
# dict={}
# max=1
# char=''
# for i in str:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# for i,j in dict.items():
#     if j>max:
#         max=j
#         char=i
# print(char)

# Implement a program to rotate a matrix (2D list) 90 degrees clockwise.

# a=[[1,2,3],
#    [4,5,6],
#    [7,8,9]]

# output
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]]


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rotated = []  # new matrix

# n = len(matrix)

# for col in range(n):
#     new_row = []
#     for row in range(n-1, -1, -1):   # bottom to top
#         new_row.append(matrix[row][col])
#     rotated.append(new_row)

# # print result
# for r in rotated:
#     print(r)
