# Find the second largest number in a list.

nums=[1,3,2,5,8,4,9,4]

first=second=0
for i in nums:
    if i>first:
        second=first
        first=i
    elif second<i and i<first:
        second=i
print(second)