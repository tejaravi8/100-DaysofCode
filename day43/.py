# n=int(input('eneter number:'))
# i=1
# while i<=n:
#     print(i)
#     i+=1

# for i in range(20,0,-1):
#     print(i)
# i=20
# n=1
# while i>=n:
#     print(i)
#     i-=1

# n=10
# sum=0
# for i in range(n,0,-1):
#     sum+=i
# print(sum)

# fact=1
# num=5
# i=1
# while i<=num:
#     fact*=i
#     i+=1
# print(fact)
# count=0
# num=int(input('enter a number:'))
# for i in range(1,num):
#     if num%i==0:
#         count+=1
#         print()

# num=5
# for i in range(2,num):
#     if num%i==0:
#         break
# else:
#     print('prime')

# count=0
# for i in range(1,101):
#     if i%2 == 0:
#         count+=1
# print(count)

# num=123456
# sum=0

# while num>0:
#     sum+=num%10
#     num//=10
# print(sum)

# num=153
# l=len(str(num))
# sum=0
# for i in str(num):
#     sum=sum+(int(i)**l)
# print(sum)


# num=154
# a=num
# count=0
# while num>0:
#     count+=1
#     num//=10

# num=a
# sum=0
# while a>0:
#     sum+=(a%10)**count
#     a//=10
# if sum==num:
#     print('armstrong')
# else:
#     print('not arm')
    
    
# name='racecar'
# rev=''
# for i in name:
#     rev=i+rev

# if name==rev:
#     print('palindrome')
# else:
#     print('not a palindrome')

  
  
i=1
count=0          
while i<=100:
    if count==10:
        i+=9
        count=0
    else:
        print(i)
        count+=1
    i+=1




n=100
count=0
for i in range(1,n+1):
    if 1<=i<10 or 21<=i<=30 or 41<=i<=50 or 61<=i<=70 or 81<=i<=90:
        print(i)

