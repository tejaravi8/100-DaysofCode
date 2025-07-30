# 5) Tuple of product of pairs (i * j) where: 
# i in [2, 4, 6] 
# j in [1, 3, 5] 


i=[2, 4, 6]
j=[1,3,5]
new=tuple(x*y for x in i for y in j)
print(new)