# # def pattern(n,c=1):
# #     if n>c:
# #         print(' * '*c)
# #         pattern(n,c+1)

# # pattern(5)


# # def alpha(rows=5,cols=0):
# #     n=65
# #     count=0
# #     if rows>cols:
# #         print(chr(n))  # single number
# #         while count<cols:
# #             print(chr(n),end='')
# #             count+=1
# #             n+=1
# #         alpha(rows,cols+1)
# # alpha()


# # for i in range(1,6):
# #     for j in range(1,i+1):
# #         print(j,end='')
# #     print()

# # A
# # BB
# # 123
# # 1234
# # *****



# n=65
# m=97
# rows=int(input('enter rows:'))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         if i<=2:
#             print(j,end=' ')
#         elif i==3:
#             print(chr(n),end=' ')
#             n+=1
#         elif i==4:
#             print(chr(m),end=' ')
#             m+=1
#         else:
#             print('*',end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print()
        
#   *   *
#    * *
#     *
#    * *
#   *   *

# c=1
# n=97
# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
i=5      
# while i>=1:
#     j=1
#     while i>=j:
#         print(i,end=' ')
#         j+=1
#     print()
#     i-=1

# 1 12 123 1234 12345

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print(end=' ')
    