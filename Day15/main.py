# students = {
#     "Ravi": {"Math": 80, "English": 70, "Science": 60},
#     "Teja": {"Math": 90, "English": 85, "Science": 75},
#     "Ajay": {"Math": 60, "English": 75, "Science": 80}
# }

# Write a program to find the student with the highest total marks.

students = {
    "Ravi": {"Math": 80, "English": 70, "Science": 60},
    "Teja": {"Math": 90, "English": 85, "Science": 75},
    "Ajay": {"Math": 60, "English": 75, "Science": 80}
}

topper=""
max=0
for i,j in students.items():
    sum=0
    for k in j.values():
        sum+=k
    if sum>max:
        max=sum
        topper=i
print(topper)