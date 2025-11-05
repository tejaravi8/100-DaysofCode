# # # import csv

# # # with open("treatments.csv","r") as f:
# # #     data=csv.reader(f)
# # #     for i in data:
# # #         print(i)

# # import csv

# # # import csv

# # with open("rai.csv", "r") as file:
# #     # reader = csv.reader(file)
# #     # for i in reader:
# #         # print(i)
# #     reader=file.read()
# #     print(reader)


# # # try:
# # #     with open("treatments.csv","r") as r,open("ravi.csv","w",newline="") as w:
# # #         w.write(r.read())
# # # except TypeError:
# # #     print("enter valid")

# import csv

# import csv

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["Name"], "got", row["Marks"])


# # with open("students.csv", "w", newline="") as file:
# #     # writer = csv.writer(file)
# #     # writer.writerow(["Name", "Age", "Marks"])  # header
# #     # writer.writerow(["Teja", 22, 90])
# #     # writer.writerow(["Ravi", 21, 85])
# #     # writer.writerow(["Babu", 23, 88])
# #     writer=csv.writer(file)
# #     writer.writerow(["papa",21,95])
# #     # file.writer(["papa",21,95])

import csv

data = [
    {"Name": "Teja", "Age": 22, "Marks": 90},
    {"Name": "Ravi", "Age": 21, "Marks": 85},
    {"Name": "Babu", "Age": 23, "Marks": 88}
]

with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
