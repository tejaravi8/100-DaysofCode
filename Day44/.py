# n=4
# i=1
# while i<=4:
#     print('* '*n)
#     i+=1

# n=4
# for i in range(n):
#     print('* '*(n*2))


# right angle triangle
# for i in range(5):
#     print('* '*i)
# i=1

# while i<=4:
#     print(i*'* ')
#     i+=1

# equilateral triangle/pyramid:
# n=4
# i=1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1
# n=5
# i=1
# while i<=n:
#     print(' '*i+(n-i)*'* ')
#     i+=1

# hallow square

n=4
i=1
while i<=n:
    if i==1 or i==n:
        print("* "*(n*2))
    else:
        print("* "+(2*(n-2))*'   '+"*")
    i+=1