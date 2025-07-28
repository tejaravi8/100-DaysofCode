#  Find the intersection and union of two lists.

a=[1,2,3,4,2,4]
b=[3,4,5,6,7,5]

# c=list(set(a+b))
# print(c)

# for i in a:
#     if i in b:
#         print(i)

a=set(a)
b=set(b)
print(a.union(b),"union")
print(a.intersection(b),"intersection")


       