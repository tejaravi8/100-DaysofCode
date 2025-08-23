# Calculate and print the average marks scored in each subject across all students.

students = {
    "Ravi": {"Math": 80, "English": 70, "Science": 60},
    "Teja": {"Math": 90, "English": 85, "Science": 75},
    "Ajay": {"Math": 60, "English": 75, "Science": 80}
}

subject_totals={"Math":0,"English":0,"Science":0}
no_students=len(students)

for j in students.values():
    for subject,mark in j.items():
        subject_totals[subject]+=mark
        
for name,avgs in subject_totals.items():
    print(f"{name}: {avgs/no_students}")
# print(subject_totals)