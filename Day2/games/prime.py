# j=[10,2,5,6,8,9]
# res={x:('prime' if all(x%y!=0 for y in range(2,x))else 'not prime') for x in j}
# print(res)

# a="b"

# print(a.upper())
res={}
p1=input("enter single char:")
if p1 in "aeiou":
    print(p1)
    
else:
    res[p1.upper()]=ord(p1.upper)
print(res)