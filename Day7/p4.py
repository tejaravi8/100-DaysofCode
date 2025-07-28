# Convert a string "1a2b3c" to "abc123".

input="1a2b3c"
num=""
alp=""
for i in input:
    if i.isdigit():
        num+=i
    else:
        alp+=i
        
print(alp+num)