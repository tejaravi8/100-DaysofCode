def get_student_data():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = []
    subjects = ['English', 'Python', 'HTML']
    
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except:
                print("Invalid input. Enter integer value.")
    return {'name': name, 'roll': roll, 'marks': marks}

def calculate_result(student):
    total = sum(student['marks'])
    average = total / len(student['marks'])
    student['total'] = total
    student['average'] = average
    
    if average >= 90:
        student['grade'] = 'A+'
    elif average >= 80:
        student['grade'] = 'A'
    elif average >= 70:
        student['grade'] = 'B'
    elif average >= 60:
        student['grade'] = 'C'
    elif average >= 40:
        student['grade'] = 'D'
    else:
        student['grade'] = 'F'

    # Pass status
    pass_subjects = sum([1 for mark in student['marks'] if mark >= 35])
    student['status'] = 'Pass' if pass_subjects >= 2 else 'Fail'

def display_all(students):
    print("\n========== Student Report Cards ==========")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}")
        print(f"Marks: {s['marks']}, Total: {s['total']}, Avg: {s['average']:.2f}")
        print(f"Grade: {s['grade']}, Status: {s['status']}")
        print("-------------------------------------------")

# Driver code
students = []
n = int(input("Enter number of students: "))
for _ in range(n):
    student = get_student_data()
    calculate_result(student)
    students.append(student)

display_all(students)
