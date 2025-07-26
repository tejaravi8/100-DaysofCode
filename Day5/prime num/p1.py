# n=10
# res=[]
# for i in range(1,100):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         res.append(i)
        
#     if len(res)==n:
#         print(res)
#         break

# n = 51
# if n > 1:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print(f"{n} is not prime")
#             break
#     else:
#         print(f"{n} is prime")  # runs only if loop completes (no divisor found)


# def check_prime(p):
#     if p<1:
#         return False
#     for i in range(2,p):
#         if p%i==0:
#             return False
#     return True      
# print(check_prime(2))

# n= 2
# upper=n
# lower=n
# while True:
#     if check_prime(upper):
#         print(upper)
#         break
#     if check_prime(lower):
#         print(lower)
#         break
#     upper+=1
#     lower-=1


# function : it is reuseable
# we can use what you want thats only
# def():
# here body in function
# next in function there are 5 types of parameters
# postional argument
# key word (argument):

# def fun(name,age):
    
#     print('name:',name)
#     print('age:',age)

# fun(age=25,name='ajay')

# default (argument):
# def fun(a=10,b=20):
    
#     print('a:',a)
#     print('b:',b)
    
# fun(b=500)

# variable length argument:
    
# def fun1(a,b):
#     print(a+b)
# fun1(10,20)

# def fun(*v): 
#     print(sum(v))
# fun(10,80)

# keyword variable length argument:
    
# def fun(**v):
#     for i,j in v.items():
#         print(i,':',j)
# fun(name='ajay',pin=210,mobile=90234122)




# n=568973
# item=0
# sum=0
# while n>0:
#     item=n%10
#     n=n//10
#     if item<1:
#         break
#     for i in range(2,item):
#         if item%i==0:
#             break
#     else:
#         # print(item)
#         sum+=item
# print(sum)

# n=568973