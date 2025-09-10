# # # Nested Dictionaries (10)

# # # Store student data {name, subjects: {sub1, sub2, sub3}} for 5 students and print the topper’s name.
# # # students={
# # #     'raviteja':{'math':90,'phy':85,'eng':75},
# # #     'durva':{'math':89,'phy':80,'eng':80},
# # #     'pablo':{'math':88,'phy':80,'eng':77},
# # #     'sailu':{'math':80,'phy':70,'eng':80},
# # #     'pallu':{'math':70,'phy':65,'eng':75}
# # # }
# # # topper=''
# # # marks=0
# # # for i,j in students.items():
# # #     sub=0
# # #     for k,l in j.items():
# # #         sub+=l
# # #     if sub>marks:
# # #         marks=sub
# # #         topper=i
# # # print(topper,marks)

# # # Do you want me to also show you how to print not just topper, but 1st, 2nd, 3rd rankers?

# # # From a dictionary of {employee: {age, salary}}, print employees earning more than 50,000.
# # # company={'teja':{'age':21,'salary':53000},
# # #          'raviteja':{'age':22,'salary':48000},
# # #          'durva':{'age':23,'salary':50000},
# # #          'ganesh':{'age':24,'salary':47000},
# # #          'pablo':{'age':25,'salary':60000}}

# # # name=[]
# # # salary=50000
# # # for i,j in company.items():
# # #     if j['salary']>salary:
# # #         name.append({i:{j['salary']}})
# # # print(name)
# # # Given a dictionary {city: {population, area}}, find the city with highest population density.

# # # Count how many students scored more than 80 in at least 2 subjects.
# # # students={
# # #     'raviteja':{'math':90,'phy':85,'eng':75},
# # #     'durva':{'math':89,'phy':80,'eng':80},
# # #     'pablo':{'math':88,'phy':80,'eng':77},
# # #     'sailu':{'math':80,'phy':70,'eng':80},
# # #     'pallu':{'math':70,'phy':65,'eng':75}
# # # }
# # # name=[]
# # # count_up=0
# # # for i,j in students.items():
# # #     count=0
# # #     for k in j.values():
# # #         if k>80:
# # #             count+=1
# # #     if count>=2:
# # #         count_up+=1
# # #         name.append(i)
# # # print(name)
        
        
# # # Update a nested dictionary to add "grade" for each student based on their average.

# # # Merge two nested dictionaries representing product stocks into one.

# # # Given {class: {student: marks}}, find average marks of each class.

# # # Sort employees by salary (nested dict).
# # company={'teja':{'age':21,'salary':53000},
# #          'raviteja':{'age':22,'salary':48000},
# #          'durva':{'age':23,'salary':50000},
# #          'ganesh':{'age':24,'salary':47000},
# #          'pablo':{'age':25,'salary':60000}
# #         }



# # # Find the student who scored the minimum in Math.
# # # students={
# # #     'raviteja':{'math':90,'phy':85,'eng':75},
# # #     'durva':{'math':89,'phy':80,'eng':80},
# # #     'pablo':{'math':88,'phy':80,'eng':77},
# # #     'sailu':{'math':80,'phy':70,'eng':80},
# # #     'pallu':{'math':70,'phy':65,'eng':75}
# # # }

# # # min=float('inf')
# # # name=''
# # # for i,j in students.items():
# # #     if j['math']<min:
# # #         min=j['math']
# # #         name=i
# # # print(min,name)
# # # # Delete a student record from a nested dictionary by name.

# # students={
# #     'raviteja':{'math':90,'phy':85,'eng':75},
# #     'durva':{'math':89,'phy':80,'eng':80},
# #     'pablo':{'math':88,'phy':80,'eng':77},
# #     'sailu':{'math':80,'phy':70,'eng':80},
# #     'pallu':{'math':70,'phy':65,'eng':75}
# # }
# # # students.pop('raviteja')
# # # print(students)


# # # new={}
# # # for i,j in students.items():
# # #     if i=='raviteja':
# # #         pass
# # #     else:
# # #         new[i]=j
# # # for i,j in new.items():
# # #     print({i:j})

# # # Given ((1,2),(3,4),(5,6)), print the sum of all elements.

# # # num=((1,2),(3,4),(5,6))
# # # sum=0
# # # for i in num:
# # #     for j in i:
# # #         sum+=j
# # # print(sum)
        
# # # Check if a nested tuple contains a specific value.
# # # num=((1,2),(3,4),(5,6))
# # # n=9
# # # a=True
# # # for i in num:
# # #     for j in i:
# # #         if j==n:
# # #             a=False
# # #             print('found')
# # #             break
# # # if a:
# # #     print('not found')
# # # Convert a nested tuple into a dictionary {index: tuple}.

# # # Swap the elements of each nested tuple → (1,2) → (2,1).

# # # Find the tuple with maximum sum of elements.

# # # Sort a list of nested tuples by the second element.

# # # Convert a nested tuple into a flat list.
# # # n=((1,(2,3)),(4,5))
# # # result=[]
# # # for i in n:
# # #     if type(i)==tuple:
# # #         for j in i:
# # #             if 
# # #             result.append(j)
# # #     else:
# # #         result.append(i)
# # # print(result)
# # # Count the frequency of elements in a nested tuple.

# # # Reverse each inner tuple.

# # # Find common elements between two nested tuples.

# # # def check(num):
# # #     if num<2:
# # #         return False
# # #     for i in range(2,num):
# # #         if num%i==0:
# # #             return False
# # #     return True
# # # print(check(6))



# # # name='he llo wor ld'
# # # new=name.split(' ')
# # # new='8'.join(new)
# # # print(new)


# # # name='hel_lo_wor_ld'
# # # new=name.split('_')
# # # new=''.join(new)
# # # print(new)

# # # name='my_variable_name'
# # # output=''
# # # # output+=name[0].upper()
# # # for i in range(1,len(name)):
# # #     if name[i-1]=="_":
# # #         output+=(name[i].upper())
# # #     elif name[i]=='_':
# # #         pass
# # #     else:
# # #         output+=name[i]
# # # print(output)

# # n='my_variable_name'
# # o=''
# # o+=n[0].upper()
# # for i in range(1,len(n)):
# #     if n[i-1]=="_":
# #         o+=n[i].upper()
# #     elif n[i]=="_":
# #         pass
# #     else:
# #         o+=n[i]
# # print(o)
    

# # n='my_VariableName'
# # o=''
# # o+=n[0].upper()
# # for i in range(1,len(n)):
# #     if n[i-1]=="_":
# #         o+=n[i].upper()
# #     elif n[i]=="_":
# #         pass
# #     else:
# #         o+=n[i]
# # print(o)

# # k="abc1234"
# # l=""
# # for i in k:
# #     if k[i]==k.isdigit:
        
        
# # # name='hello'
# # # new=''
# # # for i in name:
# # #     new=i+new
# # # print(new)
# # # # print(name[::-1])


# # name='programming'
# # new=''
# # for i in range(len(name)):
# #     count=0
# #     for j in (i,len(name)):
# #         if name[i]==name[j]:
# #             count+=1
# #     if count==1:
# #         print(name[i])
# #         break
# a='b'
# b='a'
# print(hash(a))
# print(hash(b)) 
# a=10
# a=a-10
# print(a)

# nums=[1,2,4,6,9,3,5]

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]>nums[j]:
#             nums[i],nums[j]=nums[j],nums[i]
#         else:
#             nums[i],nums[j]=nums[i],nums[j]
# print(nums)
# name='tejaat'
# for i in range(len(name)):
#     count=0
#     for j in range(len(name)):
#         if name[i]==name[j]:
#             count+=1
#     if count==1:
#         print(name[i])
#         break

# names=['ravi','durvasulu','pablo']
# new=''
# for i in names:
#     if len(new)<len(i):
#         new=i
# print(new)

# num1=15
# n2=30
# gcd=None
# for i in range(1,min(num1,n2)+1):
#     if num1%i==0 and n2%i==0:
#         gcd=i
        
# print(gcd)





