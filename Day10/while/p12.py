# 12. Using a loop, flatten [10, 20, 30, [100, 200, 300], 50, 60] the list into a single list → [10, 20, 
# 30, 100, 200, 300, 50, 60].

nums=[10,20,30,[100,200,300],50,60]

flat = []

# for item in nums:
#     if isinstance(item, list):
#         for subitem in item:
#             flat.append(subitem)
#     else:
#         flat.append(item)

# print(flat)

for  i in nums:
    if type(i)==list:
        flat.extend(i)
    else:
        flat.append(i)
print(flat)

