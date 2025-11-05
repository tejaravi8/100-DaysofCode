# import json
# data={
#     "name":"raviteja",
#     "age":21,
#     "marks":81
# }

# with open("teja.json","r") as file:
#     f=json.load(file)
#     print(f["age"])
    
    
# import json

# data = {"name": "Teja", "city": "Hyderabad", "skills": ["Python", "SQL"]}

# with open("pretty.json", "w") as file:
#     json.dump(data, file, indent=4)

# import json

# students = [
#     {"name": "Teja", "marks": 90},
#     {"name": "Ravi", "marks": 85},
#     {"name": "Babu", "marks": 88}
# ]

# with open("students.json", "w") as f:
#     json.dump(students, f, indent=4)

import json

with open("students.json", "r") as f:
    data = json.load(f)
# print(data)
for s in data:
    print(s["name"], "got", s["marks"])
