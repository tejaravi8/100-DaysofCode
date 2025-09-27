# # # # # # # a=[5, 10, 15, 20, 1]
# # # # # # # # # a.extend([1,2])
# # # # # # # # # a.insert(1,55)
# # # # # # # # # a[0]=1
# # # # # # # # del a[1:4]
# # # # # # # # # del a[1]
# # # # # # # # # a.pop(-1)
# # # # # # # # print(a)

# # # # # # a=[i**3 for i in range(1,6)]
# # # # # # print(a)

# # # # # # mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # # # # # for row in mat:
# # # # # #     # print(row)
# # # # # #     for num in row:
# # # # # #         # print(num)

# # # # # # new=[j for i in mat for j in i]
# # # # # # print(new)

# # # # # # new=[i for i in range(1,11)]
# # # # # # print(new)

# # # # # # a={41, 10, 26, 54}
# # # # # # a.clear()
# # # # # # print(a)

# # # # # # set1 = {2, 6, 3, 4, 5}
# # # # # # set1.pop(5)

# # # # # # fset = frozenset([1, 2, 3, 4, 5, 1, 1, 1 ])
# # # # # # print(fset)
# # # # # # print(set1)
# # # # # # val = set1.pop()
# # # # # # print(val)
# # # # # # print(set1)

# # # # # # Using pop on an empty set
# # # # # # set1.clear()  # Clear the set to make it empty
# # # # # # try:
# # # # # #     set1.pop()
# # # # # # except KeyError as e:
# # # # # #     print("Error:", e)

# # # # # # a=[[j*i] for i in range(1,10) for j in range()]
# # # # # from collections import Counter
# # # # # # Create a list of items
# # # # # # num = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# # # # # # Use Counter to count occurrences
# # # # # # cnt = Counter(num)
# # # # # # print(collections)

# # # # # # tup = (1, 2, 3, 4)
# # # # # # # t=(5,6,7,8,)*3
# # # # # # # print(t)
# # # # # # tup(1)==0
# # # # # # print(tup)
# # # # # # a, *b, c = tup

# # # # # # print(a) 
# # # # # # print(b) 
# # # # # # for i in b:
# # # # # #     print(i)
# # # # # # print(c)

# # # # # # x,y,z=(1,2,3)
# # # # # # print(x,y,z)

# # # # # d = { "name": "Pablo", 1: "Python", (1, 2): [1,2,4] }
# # # # # print(d.get('nam','teja'))

# # # # original = {1: 'geeks', 2: 'for'}

# # # # # copying using copy() function
# # # # new = original.copy()
# # # # print(new)

# # # import copy

# # # # Python program to demonstrate difference
# # # # between = and copy()
# # # original = {1: 'geeks', 2: 'for'}

# # # # copying using copy() function
# # # new = copy.deepcopy(original)

# # # # removing all elements from new list
# # # # and printing both
# # # new.clear()
# # # print('new: ', new)
# # # print('original: ', original)

# # # original = {1: 'one', 2: 'two'}

# # # # copying using =
# # # new = original

# # # # removing all elements from new list
# # # # and printing both
# # # new.clear()
# # # print('new: ', new)
# # # print('original: ', original)

# # Store student data {name, subjects: {sub1, sub2, sub3}} for 5 students and print the topper’s name.
# students={'ravi':{'math':57,'sci':39,'eng':27},
#           'ramesh':{'math':59,'sci':68,'eng':82},
#           'raju':{'math':25,'sci':80,'eng':35},
#           'rani':{'math':33,'sci':38,'eng':87},
#           'rahul':{'math':100,'sci':18,'eng':17}
#           }
# # marks=0
# # topper=''
# # s=0
# # for it,j in students.items():
# #     s=sum(j.values())
# #     if s>marks:
# #         marks=s
# #         topper=it
# # print(topper)
#         # s=0
# # print(topper,marks)
# #     s=0
# #     for k,l in j.items():
# #         s+=l
# #     if s>marks:
# #         marks=s
# #         topper=i
# # print(topper)

        
# # From a dictionary of {employee: {age, salary}}, print employees earning more than 50,000.
# m=0
# h=''
# employees={
#           'ravi':{'age':57,'salary':39000},
#           'ramesh':{'age':59,'salary':68000},
#           'raju':{'age':25,'salary':80000},
#           'rani':{'age':33,'salary':38000},
#           'rahul':{'age':100,'salary':18000}
#           }
# for i,j in employees.items():
#     if j['salary']>50000:
#         print((j['salary'],i))
        
# # Given a dictionary {city: {population, area}}, find the city with highest population density.
# locations={'hybd':{10101018,'kphb'},
#            'vizag':{1234431,'madhurawada'},
#            'bvv':{1234567823456,'home'}
#            }
# pop=0
# loc=''
# for i,j in locations.items():
#     for k in j:
#         if type(k)==int and k>pop:
#             pop=k
#             loc=i
# print(pop,loc)
            

# # Count how many students scored more than 80 in at least 2 subjects.
students={'ravi':{'math':57,'sci':39,'eng':57},
          'ramesh':{'math':59,'sci':68,'eng':82},
          'raju':{'math':25,'sci':80,'eng':35},
          'rani':{'math':33,'sci':38,'eng':87},
          'rahul':{'math':100,'sci':18,'eng':17}
          }
# max=0
# n=[]
# for i,j in students.items():
    
#     if len([k for k in j.values() if k>50])>=2:
#         max+=1
#         n+=[i]
# print(max,n)
# # Update a nested dictionary to add "grade" for each student based on their average.
students={'ravi':{'math':57,'sci':39,'eng':57},
          'ramesh':{'math':59,'sci':68,'eng':82},
          'raju':{'math':25,'sci':80,'eng':35},
          'rani':{'math':33,'sci':38,'eng':87},
          'rahul':{'math':100,'sci':18,'eng':17}
          }
s2={    'kavya':{'math': 57, 'sci': 39, 'eng': 57, 'grade': 'A'},
        'keerthana':{'math': 59, 'sci': 68, 'eng': 82, 'grade': 'A'},
        'kaveri':{'math': 25, 'sci': 80, 'eng': 35, 'grade': 'F'},
        'krishnaveni':{'math': 33, 'sci': 38, 'eng': 87, 'grade': 'A'},
        'krithi':{'math': 100, 'sci': 18, 'eng': 17, 'grade': 'F'}
        }

# students.update(s2)
# for i in students:
    # print(i)
# s={**students,**s2}
# for i in s:
#     print(i)
# print(s)
# for i,j in students.items():
#     s=len(j)
#     su=sum(j.values())
#     avg=su/s
#     if avg>50:
#         students[i]['grade']='A'
#     else:
#         students[i]['grade']='F'

# for j in students.values():
#     print(j)
    
    # if avg>50:
    #     students[j]
    
# # Merge two nested dictionaries representing product stocks into one.

# # Given {class: {student: marks}}, find average marks of each class.

# # Sort employees by salary (nested dict).
employees = {
    "emp1": {"name": "Alice", "salary": 60000},
    "emp2": {"name": "Bob", "salary": 80000},
    "emp3": {"name": "Charlie", "salary": 50000},
    "emp4": {"name": "David", "salary": 75000},
}

sorted_employees = sorted(employees.items(), key=lambda item: item[1]["salary"])

print(sorted_employees)
# # Find the student who scored the minimum in Math.

# # Delete a student record from a nested dictionary by name.
employees=dict(sorted_employees)
del employees['emp2']
print(employees)