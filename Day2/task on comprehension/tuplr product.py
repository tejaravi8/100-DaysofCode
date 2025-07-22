# 9.	Tuple of product of pairs (i * j) where:

i = [2, 4, 6]
j = [1, 3, 5]
 
res=tuple((a*b) for a,b in zip(i,j))
print(res)