# Given [[1,2,3],[4,5,6],[7,8,9]], flatten it into a single list.
# a=[1,[2,[3,4]],[[5,6],[7,8]]]

# new=[]
# def nested(n):
#     for i in n:
#         if type(i)==list:
#             for j in i:
#                 if type(j)==list:
#                     new.extend(j)
#                 else:
#                     new.append(j)
#         else:
#             new.append(i)
#     print(new)

# nested(n=[1,[2,[3,4]],[[5,6],[7,8]]])

            
def nested(n):
    new=[]
    for i in n:
        if type(i)==list:
            new.extend(nested(i))
        else:
            new.append(i)
    return new

print(nested([1,[2,[3,4]],[[5,6],[7,8]]]))

# Find the row-wise maximum in a 2D list.

# matrix=[[3,6,7],
#         [9,8,4],
#         [8,7,2]]

# new=[]
# for i in matrix:
#     maximum=0
#     for j in i:
#         if j>maximum:
#             maximum=j
#     new.append((maximum,i))
    
# print(new)
        
# Rotate a 2D list (matrix) by 90 degrees.

# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# #[[7,4,1],
# # [8,5,6],
# # [9,6,3]]

# rows=len(mat)
# cols=len(mat[0])

# rotated=[[0 for i in range(rows)] for i in range(cols)]

# for i in range(rows):
#     for j in range(cols):
#         rotated[j][rows-1-i]=mat[i][j]
        
# for row in rotated:
#     print(row)

def oddeven(n):
    if n%2==0:
        return True
    else:
        return False
    
# Count how many even numbers are in a 2D list.
# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# count=0
# for i in mat:
#     for j in i:
#         if oddeven(j)==True:
#             count+=1
# print(count)
        

# Print the sum of each column in a matrix.
# mat=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]

# new=[]
# for i in mat:
#     s=0
#     for j in i:
#         s+=j
#     new.append(s)
# print(new)
        
# Find diagonal elements of a square matrix.
# mat=[[1,2,3,4],
#      [4,5,6,7],
#      [7,8,9,9],
#      [10,11,12,13]]

# rows=len(mat)
# cols=len(mat[0])

# for i in range(rows):
#     for _ in range(cols):
#         print(mat[i][i])
#         break
    
# Search for an element in a 2D list and return its position.

# mat =[[1,2,3,4],[21,5,6,22],[7,8,9,14],[10,11,12,13]]
# def position(n,m):
#     rows=len(n)
#     cols=len(n[0])
#     for i in range(rows):
#         for j in range(cols):
#             if n[i][j]==m:
#                 return ((i+1,j+1))
# print(position(n=mat,m=6))


# Replace all negative numbers in a 2D list with 0.
# mat =[[-1,2,3,4],
#       [21,-5,6,22],
#       [7,8,-1,14],
#       [10,11,12,-13]]
# rows=len(mat)
# cols=len(mat[0])
# for i in range(rows):
#     for j in range(cols):
#         if mat[i][j]<0:
#             mat[i][j]=0
# for row in mat:
#     print(row)
# Add two matrices (nested lists).
# mat1=[[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# mat2=[[1,2,3],
#       [4,5,6],
#       [7,8,9]]

     
# rows=len(mat1)
# cols=len(mat1[0])
# add_mat=[]
# for i in range(rows):
#     new=[]
#     for j in range(cols):
#         a=mat1[i][j]+mat2[i][j]
#         new.append(a)
#     add_mat.append(new)

# print(add_mat)
        

# Convert a 2D list into a dictionary with row index as key.

# mat1=[[1,2,3],
#       [4,5,6],
#       [7,8,9]]

# dict={}
# for i in range(len(mat1)):
#     dict[i]=mat1[i]
    
# print(dict)
        
    
    
# Write a program to flatten a nested list.
# new=[]

# def check(n):
#     for i in n:
#         if type(i)==list:
#             check(i)
#         else:
#             new.append(i)
# check(n=[1,[2,3],[4,[5,6]]])
# print(new)

# n=[1,[2,3],[4,[5,6]]]
# n=[1,[2,[3,4]],[[5,6],[7,8]]]
# new=[]   
# for i in n:
#     if type(i)==list:
#         for j in i:
#             if type(j)==list:
#                 new.extend(j)
#             else:
#                 new.append(j)
#     else:
#         new.append(i)
# print(new)



n=[9,9,9,9]
c=1
sol=[]
for i in range(len(n)-1,-1,-1):
    if n[i]+c>9:
        sol.append(0)
        c=1
    else:
        sol.append(n[i]+c)
        c=0
if c:
    sol.append(c)
sol.reverse()
print(sol)