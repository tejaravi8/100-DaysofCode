# Nested Dictionaries (10)

# Store student data {name, subjects: {sub1, sub2, sub3}} for 5 students and print the topper’s name.
# students={
#     'raviteja':{'math':90,'phy':85,'eng':75},
#     'durva':{'math':89,'phy':80,'eng':80},
#     'pablo':{'math':88,'phy':80,'eng':77},
#     'sailu':{'math':80,'phy':70,'eng':80},
#     'pallu':{'math':70,'phy':65,'eng':75}
# }
# topper=''
# marks=0
# for i,j in students.items():
#     sub=0
#     for k,l in j.items():
#         sub+=l
#     if sub>marks:
#         marks=sub
#         topper=i
# print(topper,marks)

# Do you want me to also show you how to print not just topper, but 1st, 2nd, 3rd rankers?

# From a dictionary of {employee: {age, salary}}, print employees earning more than 50,000.
# company={'teja':{'age':21,'salary':53000},
#          'raviteja':{'age':22,'salary':48000},
#          'durva':{'age':23,'salary':50000},
#          'ganesh':{'age':24,'salary':47000},
#          'pablo':{'age':25,'salary':60000}}

# name=[]
# salary=50000
# for i,j in company.items():
#     if j['salary']>salary:
#         name.append({i:{j['salary']}})
# print(name)
# Given a dictionary {city: {population, area}}, find the city with highest population density.

# Count how many students scored more than 80 in at least 2 subjects.
# students={
#     'raviteja':{'math':90,'phy':85,'eng':75},
#     'durva':{'math':89,'phy':80,'eng':80},
#     'pablo':{'math':88,'phy':80,'eng':77},
#     'sailu':{'math':80,'phy':70,'eng':80},
#     'pallu':{'math':70,'phy':65,'eng':75}
# }
# name=[]
# count_up=0
# for i,j in students.items():
#     count=0
#     for k in j.values():
#         if k>80:
#             count+=1
#     if count>=2:
#         count_up+=1
#         name.append(i)
# print(name)
        
        
# Update a nested dictionary to add "grade" for each student based on their average.

# Merge two nested dictionaries representing product stocks into one.

# Given {class: {student: marks}}, find average marks of each class.

# Sort employees by salary (nested dict).
company={'teja':{'age':21,'salary':53000},
         'raviteja':{'age':22,'salary':48000},
         'durva':{'age':23,'salary':50000},
         'ganesh':{'age':24,'salary':47000},
         'pablo':{'age':25,'salary':60000}
        }



# Find the student who scored the minimum in Math.
# students={
#     'raviteja':{'math':90,'phy':85,'eng':75},
#     'durva':{'math':89,'phy':80,'eng':80},
#     'pablo':{'math':88,'phy':80,'eng':77},
#     'sailu':{'math':80,'phy':70,'eng':80},
#     'pallu':{'math':70,'phy':65,'eng':75}
# }

# min=float('inf')
# name=''
# for i,j in students.items():
#     if j['math']<min:
#         min=j['math']
#         name=i
# print(min,name)
# # Delete a student record from a nested dictionary by name.

students={
    'raviteja':{'math':90,'phy':85,'eng':75},
    'durva':{'math':89,'phy':80,'eng':80},
    'pablo':{'math':88,'phy':80,'eng':77},
    'sailu':{'math':80,'phy':70,'eng':80},
    'pallu':{'math':70,'phy':65,'eng':75}
}
# students.pop('raviteja')
# print(students)


# new={}
# for i,j in students.items():
#     if i=='raviteja':
#         pass
#     else:
#         new[i]=j
# for i,j in new.items():
#     print({i:j})