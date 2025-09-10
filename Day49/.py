# def check(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True


# n=23579812
# a=n
# rev=0
# while n>0:
    
    
# prime=None
# while n>0:
#     prime=n%10
#     if check(prime):
#         print(prime)
#     n//=10
#     prime=None



# name='ravi_teja_botsa'
# new=''
# new=name[0].upper()
# for i in range(len(name)):
#     if name[i-1]=='_':
#         new+=name[i].upper()
#     elif name[i]=='_':
#         pass
#     else:
#         new+=name[i]
# print(new)


# name='World Health Organisation'
# new=''

# for i in name:
#     if i.upper()==i and i!=' ':
#         new+=i+'.'
# print(new)


# name='World Health Organisation'
# new=''
# new=name[0].upper()+'.'
# for i in range(len(name)):
#     if name[i-1]==' ':
#         new+=name[i]+'.'

# print(new[:len(new)-1])


# sum of factorial = same number

# num=40585
# n=num
# sum=0
# while num>0:
#     fact=1
#     a=(num%10)
#     i=1
#     while i<=a:
#         fact*=i
#         i+=1
#     sum+=fact
#     num//=10
# print(sum==n)
n=5
for i in range(5):
    print(' '*(i*2)+'*'+' '*(n-i*2)+'*')