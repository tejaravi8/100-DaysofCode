# Extract all numbers from a string and calculate their sum. 
# "abc12xyz34" → Output: 46

input="abc12xyz34"
a=""
sum=0
for i in input:
    if i.isdigit():
        a+=i
b=a[0:2]+" "+a[2:]
x=b.split(" ")
print(x)
for i in x:
    sum+=int(i)
print(sum)
# print(b)