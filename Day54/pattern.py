# # # # def pattern(n,c=1):
# # # #     if n>c:
# # # #         print(' * '*c)
# # # #         pattern(n,c+1)

# # # # pattern(5)


# # # # def alpha(rows=5,cols=0):
# # # #     n=65
# # # #     count=0
# # # #     if rows>cols:
# # # #         print(chr(n))  # single number
# # # #         while count<cols:
# # # #             print(chr(n),end='')
# # # #             count+=1
# # # #             n+=1
# # # #         alpha(rows,cols+1)
# # # # alpha()


# # # # for i in range(1,6):
# # # #     for j in range(1,i+1):
# # # #         print(j,end='')
# # # #     print()

# # # # A
# # # # BB
# # # # 123
# # # # 1234
# # # # *****



# # # n=65
# # # m=97
# # # rows=int(input('enter rows:'))
# # # for i in range(1,rows+1):
# # #     for j in range(1,i+1):
# # #         if i<=2:
# # #             print(j,end=' ')
# # #         elif i==3:
# # #             print(chr(n),end=' ')
# # #             n+=1
# # #         elif i==4:
# # #             print(chr(m),end=' ')
# # #             m+=1
# # #         else:
# # #             print('*',end=' ')
# # #     print()


# # # for i in range(1,6):
# # #     for j in range(1,i+1):
# # #         print()
        
# # #   *   *
# # #    * *
# # #     *
# # #    * *
# # #   *   *

# # # c=1
# # # n=97
# # # rows=5
# # # for i in range(1,rows+1):
# # #     for j in range(1,i+1):
# # i=5      
# # # while i>=1:
# # #     j=1
# # #     while i>=j:
# # #         print(i,end=' ')
# # #         j+=1
# # #     print()
# # #     i-=1

# # # 1 12 123 1234 12345

# # # for i in range(5,0,-1):
# # #     for j in range(1,i+1):
# # #         print(j,end='')
# # #     print(end=' ')
    
# # # a
# # # bb
# # # ccc
# # # dddd
# # # eeeee

# # # num=65
# # # for i in range(1,6):
# # #     for j in range(1,i+1):
# # #         print(chr(num),end='')
# # #     print()
# # #     num+=1

# # # num=65
# # # for i in range(1,6):
# # #     for j in range(1,i+1):
# # #         print(chr(num),end='')
# # #         num+=1
# # #     print()

# # # alpha=input('enter a charecter:')
# # # num=ord(alpha)

# # # for i in range(1,6):
# # #     for j in range(1,i+1):
# # #         print(chr(num),end='')
# # #         num+=1
# # #     print(end=' ')

# # # for i in range(5):
# # #     for i in range(1,6):
# # #         for j in range(1,i+1):
# # #             print("* ",end=' ')
# # #             # print(' '*(6-i)+'*',end='')
# # #         print()
# # #     for i in range(4,-1,-1):
# # #         for j in range(1,i+1):
# # #             print("* ",end=' ')
# # #             # print(' '*(6-i)+'*',end='')
# # #         print()


# # # n=5
# # # for i in range(1,n+1):
# # #     for j in range(1,i+1):
# # #         print(' '*(n-i),end=' ')
# # #     print('*'*i)

# # 1
# # 21
# # 321
# # 4321
# # 54321


# # rows = 5
# # for i in range(1, rows+1):
# #     # print spaces
# #     print("  " * (rows - i), end="")
# #     # print stars
# #     print("* " * i)

# # rows = 5
# # for i in range(1, rows+1):   # outer loop for rows
# #     for j in range(1, rows+1):   # inner loop for spaces + stars
# #         if j <= rows - i:
# #             print(" ", end="")   # print spaces
# #         else:
# #             print("*", end=" ")  # print stars
# #     print()   # move to next line


# rows=5

# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print('* ',end='')
    
#     print()

# for i in range(1,rows):
#     for j in range(1,rows+1):
#         if j<=rows-i:
#             print('  ',end='')
#         else:
#             print(' *',end='')
#     print()


# for i in range(rows,-1,-1):
#     for j in range(1,rows+1):
#         if j<=rows-i:
#             print('  ',end='')
#         else:
#             print(' *',end='')
#     print()

# # rows = 5
# # for i in range(1, rows+1):
# #     # print spaces
# #     print(" " * (rows - i), end="")
# #     # print stars
# #     print("* " * i)

# # for i in range(1,rows+1):
# #     print('  '*(rows-i),end='')
# #     print("* "*i)

rows = 5  # middle row stars

# Upper half
for i in range(1, rows+1):
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(1, 2*(rows-i)):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()