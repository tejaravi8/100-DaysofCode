# Input b=[[1, 2], [3, 4], [5, 6]]     out put=[1,2,3,4,5,6] 

b=[[1, 2], [3, 4], [5, 6]]
new=[j for i in b for j in i]
print(new)