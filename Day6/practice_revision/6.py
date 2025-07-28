# Print all keys and values in a dictionary.

students = {
    "Ravi": 78,
    "Teja": 85,
    "Kiran": 92,
    "Nikhil": 67,
    "Arjun": 49
}

# for i,j in students.items():
#     print(f"{i}:{j}")
    
# 7.Count how many students scored above 50   
count=sum([1 for i in students.values() if i>50])
print(count)

# 8.Find the student with the highest marks


# count = sum(1 for m in students.values() if m > 50)
# print("Students scoring above 50:", count)

