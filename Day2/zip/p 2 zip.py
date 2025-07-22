# Sum corresponding elements of two lists using zip().

a=[10,33,25,43]
b=[11,34,26,44]

r=[i+j for i,j in zip(a,b)]
print(r)