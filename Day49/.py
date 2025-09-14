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

# # print(new)
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
# n=5
# for i in range(5):
#     print(' '*(i*2)+'*'+' '*(n-i*2)+'*')

# num=153
# new=0
# c=len(str(num))
# for i in str(num):
#     new+=int(i)**c

# print(new)

# num=int(input('eneter a number:'))
# a=num
# n=a
# c=0
# while num>0:
#     c+=1
#     num=num//10

# while a>0:
#     num+=(a%10)**c
#     a//=10

# if num==n:
#     print(f"{n} is armstrong")
# else:
#     print(f"{n} is not armstrong")

# num=153
# rev=0
# while num>0:
#     rev=(num%10)+rev*10
#     num//=10
# print(rev)

# num=26
# check=0
# for i in range(1,num):
#     if num%i==0:
#         check+=i
# if num==check:
#     print('perfect')
# else:
#     print()

# num=1
# sqre=num**2
# sum=0
# while sqre>0:
#     sum+=sqre%10
#     sqre//=10
# if sum==num:
#     print('neon number')

# num=1
# new=num**2
# sum=0
# for i in str(new):
#     sum+=int(i)
# print(sum==num)

# num=19
# temp=num
# sum=0
# while temp>0:
#     sum+=temp%10
#     temp//=10
# if num%sum==0:
#     print('harshad number')
# else:
#     print('not an harshad')
# a,b=0,1
# for i in range(5):
#     print(a)
#     a,b=b,a+b


# a,b=0,1
# i=1
# while i<=10:
#     print(a)
#     a,b=b,a+b
#     i+=1