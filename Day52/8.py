# # # # # # # # # matrix=[[1, 2,3], [4, 5,6],[7,8,9]]

# # # # # # # # # row=len(matrix[0])
# # # # # # # # # col=len(matrix)
# # # # # # # # # # print(row,col)


# # # # # # # # # # if row==col:
# # # # # # # # # #     print('square')
# # # # # # # # # # else:
# # # # # # # # # #     print('not a square matrix')
    
    
# # # # # # # # # # : Print the main diagonal elements of a square matrix

# # # # # # # matrix=[[1,2],[3,4]]
# # # # # # # if len(matrix)==len(matrix[0]):

# # # # # # # for i in range(len(matrix)):
# # # # # # #     for j in range(len(matrix[i])):
# # # # # # #         if i==j:
# # # # # # #             print(matrix[i][j])
            
# # # # # # # # # # non - diagnol
# # # # # # # # # for i in range(len(matrix)):
# # # # # # # # #     for j in range(len(matrix[i])):
# # # # # # # # #         if i!=j:
# # # # # # # # #             print(matrix[i][j])

# # # # # # # # # anti-diagnol


# # # # # # # # # # multiplication


# # # # # # # a = [[1, 2],
# # # # # # #      [3, 4]]

# # # # # # # b = [[5, 6],
# # # # # # #      [7, 8]]

# # # # # # # rows_a=len(a)
# # # # # # # cols_a=len(a[0])
# # # # # # # rows_b=len(b)
# # # # # # # cols_b=len(b[0])

# # # # # # # result=[[0 for _ in range(cols_b)] for _ in range(rows_a)]

# # # # # # # if cols_a != rows_b:
# # # # # # #     print('multiplication not possible')
# # # # # # # else:
# # # # # # #     for i in range(rows_a):
# # # # # # #         for j in range(cols_b):
# # # # # # #             for k in range(cols_b):
# # # # # # #                 result[i][j]+=a[i][k]*b[k][j]

# # # # # # # # print(result)


# # # # # # # # cols=4
# # # # # # # # a=cols
# # # # # # # # rows=5
# # # # # # # # new=[]
# # # # # # # # i=1
# # # # # # # # while rows>=1:
# # # # # # # #     sub=[]
# # # # # # # #     while cols>=1:
# # # # # # # #         sub.append(i) 
# # # # # # # #         i+=1
# # # # # # # #         cols-=1
# # # # # # # #     new.append(sub)
# # # # # # # #     cols=a
# # # # # # # #     rows-=1
# # # # # # # # print(new)

# # # # # # # # nums=[1,2,3,4,5,6]
# # # # # # # # x=[]
# # # # # # # # y=[]
# # # # # # # # c=0
# # # # # # # # for i in nums:
# # # # # # # #     if c<=1:
# # # # # # # #         y.append(i)
# # # # # # # #         c+=1
# # # # # # # #     else:
# # # # # # # #         x.append(y)
# # # # # # # #         y=[i]
# # # # # # # #         c=1
# # # # # # # # x.append(y)
# # # # # # # # print(x)
        
# # # # # # # # for i in nums:
# # # # # # # #     if len(y)<=1:
# # # # # # # #         y.append(i)
# # # # # # # #     else:
# # # # # # # #         x.append(y)
# # # # # # # #         y=[i]
# # # # # # # # x.append(y)
# # # # # # # # print(x)


        
# # # # # # a=[[5, 0, 8], 
# # # # # #    [0, 7, 2],
# # # # # #    [1, 1, 6]]



# # # # # # rows=len(a)
# # # # # # d=[a[i][i] for i in range(rows)]
# # # # # # print(d)

# # # # # # a=any(d[0]==i for i in d)
# # # # # # print(a)
    
# # # # # # # cols=len(a[0])
# # # # # # # if rows!=cols:
# # # # # # #     print('not possible')
# # # # # # # else:
# # # # # # #     for i in range(1,rows):
# # # # # # #         if a[i-1][i-1]==a[i][i]:
# # # # # # #             print('diagnols are same')


# # # # # # a=[[0, 3], 
# # # # # #    [3, 0]]
# # # # # # cols=len(a[0])
# # # # # # rows=len(a)
# # # # # # # matrix=[a[i-1][i-1]  ]

# # # # # # c=[]
# # # # # # for i in range(1,rows):
# # # # # #     for j in range(cols):
# # # # # #         if a[i-1][j] ==a[i][j]:
# # # # # #             c.append(a[i-1][j])
# # # # # # print(c)

# # # # # a = [[5, 0, 8],
# # # # #      [0, 7, 2],
# # # # #      [1, 1, 6]]

# # # # # for i,row in enumerate(a):
# # # # #     print(i,row)


# # # # # # n=len(a)
# # # # # # for i in range(len(a)):
# # # # # #     print(a[i][n-1-i])

# # # a = [[5, 0, 8],
# # #      [0, 7, 2],
# # #      [1, 1, 6]]

# # # flat = [x for row in a for x in row]
# # # print(flat)


# # # # # rows, cols = len(a), len(a[0])
# # # # # transpose = [[a[r][c] for r in range(rows)] for c in range(cols)]
# # # # # print(transpose)
# # # # # rows = len(a)        # 3
# # # # # cols = len(a[0])

# # # # # for i, row in enumerate(a):
# # # # #     for j, val in enumerate(row):
# # # # #         print(i,j,val)
# # # # #         # use i, j, val here


# # a = [[1, 2, 3],
# #      [4, 5, 6],
# #      [7, 8, 9]]

# # # row_sum=[sum(row) for row in a]
# # # print(row_sum)

# # c=len(a[0])
# # r=len(a)
# # cols_sum=[sum(a[r][c] for r in range(r)) for c in range(c)]
# # print(cols_sum)

# a = [[1, 2, 3],
#      [4, 5, 6]]
# r=len(a)
# c=len(a[0])
# t=[[a[c][r] for r in range(r)] for c in range(c)]

# print(t)

a = [[1, 2, 3],
     [2, 5, 6],
     [3, 6, 9]]
r=len(a)
c=len(a[0])

symmetric=all([a[r][c] for r in range(r)] for c in range(c))
print(symmetric)