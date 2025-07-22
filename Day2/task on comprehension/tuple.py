# # 1.	Create a tuple of squares of numbers from 1 to 15 using comprehension.

res=tuple(i**2 for i in range(1,16))
print(res)
# ---------------------------------------------------------------------------------

# 2.	 Given a string "Python", create a tuple of ASCII values for each character.
#  	Input b=[[1, 2], [3, 4], [5, 6]]     out put=[1,2,3,4,5,6]
#  	r=[1,2,3,4,] p=[10,20,30,40]   output=[11,12,13,14]

a=tuple((ord(i),i) for i in "Python")
print(a)

# a="Python"
# for i in a:
#     print(ord(i),i)
            
b=[[1, 2], [3, 4], [5, 6]]
output=[]

for i in b:
    output+=i
print(output)
# -------------------------------------------------------------------------
r=[1,2,3,4,]
p=[10,20,30,40]
output=[i+j for i,j in zip(r,p)]
print(output)

r=[1,2,3,4,]
output=[]
for i in r:
    output.append(i+10)
# ---------------------------------------------------------------------------
for i,j in zip(r,p):
    output.append(i+j)





