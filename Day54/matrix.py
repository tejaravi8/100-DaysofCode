# # a=[[1, 2], [3, 4]]
# # rows=len(a)
# # cols=len(a[0])
# # if rows==cols:
# #     print('square')


# # x=[]

# # for i in range(cols):
# #     sum=0
# #     for j in range(rows):
# #         sum+=a[j][i]
# #     x.append(sum)
# # print(x)

# # for i in a:
# #     sum=0
# #     for j in i:
# #         sum+=j
# #     x.append(sum)
# # print(x)

# # diagnol=[]
# # for i in range(rows):
# #     diagnol.append(a[i][])
# # #     diagnol.append(a[i][i])
# # print(diagnol)

# # a=[[1, 2,5], [3, 4,6],[7,8,9]]
# # rows=len(a)
# # cols=len(a[0])

# # nondiagnol=[]
# # for i in range(rows):
# #     for j in range(cols):
# #         if (rows-1-i)!=j:
# #             nondiagnol.append(a[i][j])
# # print(nondiagnol)


# # a=[]
# # rows=5
# # cols=5
# # num=1
# # for i in range(rows):
# #     new=[]
# #     for j in range(cols):
# #         if rows-1-i==j:
# #             new.append(1)
# #         else:
# #             new.append(0)
# #     a.append(new)
# # # print(a)
# # for i in a:
# #     print(i)

# a = [[1, 2], 
#      [3, 4]]

# result=[]
# for i in range(len(a)):
#     new=[]
#     for j in range((len(a[0]))):
#         if i<=j:
#             new.append(a[i][j])
#         else:
#             new.append(0)
#     result.append(new)

# for i in result:
    
#     print(i)



# # rows_a=len(a)
# # cols_a=len(a[0])
# # rows_b=len(b)
# # cols_b=len(b[0])
# # result=[[0 for i in range(rows_a)] for j in range(rows_b)]
# # print(result)

# # for i in range(rows_a):
# #     for j in range(cols_b):
# #         for k in range(cols_a):
# #             result[i][j]+=a[k][i]*b[j][k]
# # print(result)

