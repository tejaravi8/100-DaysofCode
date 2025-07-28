#  Find the intersection and union of two lists.

a=[1,2,3,4]
b=[3,4,5,6]

c=list(set(a+b))
print(c)

for i in a:
    if i in b:
        print(i)
        
       