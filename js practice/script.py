# num=13
# def check(n):
#     if n<2:
#         return False
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 return False
#             else:
#                 return True

# # print(check(num))
# num=153
# c=0
# arm=0
# for i in str(num):
#     c+=1
# for i in str(num):
#     arm+=int(i)**c
# print(arm)
# except TypeError:
#     print("unsupported operation")
# else:
#     print("done")
# finally:
#     print("program done")
# ar=0
# l=len(str(num))
# while num>0:
#     rev=num%10
#     ar+=rev**l
#     num//=10

# print(ar)
        
        
# num=5
# fact=1
# for i in range(1,num+1):
#     fact*=i

# print(fact)

# a=9
# b=6

# a,b=b,a
# print(b)

# a,b=0,1
# for i in range(10):
#     print(b)
#     a,b=b,a+b

# a="Silent"
# b="Listen"

# print(sorted(a.lower())==sorted(b.lower()))

# a=[2, 4, 3, 5, 7, 8, 9]
# b=7

# for i in a:
#     for j in a:
#         if(i+j)==b:
#             print(i,j)