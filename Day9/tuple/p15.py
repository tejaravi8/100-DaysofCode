# r=[1,2,3,4,] p=[10,20,30,40]   output=[11,12,13,14] 

r=[1,2,3,4,] 
p=[10,20,30,40]
a=list(i+j for i,j in zip(r,p))
print(a)

# new=[r[i]+p[i] for i in range(0,len(r))]
# print(new)