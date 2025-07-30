#    From the string "Hello World", create a set of unique characters. 

a="Hello World"
b=""
for i in a:
    if i !=" ":
        b+=i
             
print(set(b))