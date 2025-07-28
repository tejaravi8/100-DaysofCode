# Convert a string to title case without using .title(). 
# Input: "python is fun" → Output: "Python Is Fun"

input="python is fun"
a=input.split()
rev=""
# print(a)
for i in a:
    rev+=i.capitalize()+" "
print(rev)