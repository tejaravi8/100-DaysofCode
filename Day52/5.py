# num1=int(input('enter a number:'))
# num2=int(input('enter a number:'))

# while num1<=(num2):
#     count=0
#     i=2
#     while i<num1:
#         if num1%i==0:
#             count+=1
#         i+=1
#     if count==0:
#         print(num1)
    
#     num1+=1

# num1=5
# num2=11
# count=0
# for i in range(num2,num1-1,-1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
#         count+=1
# print(count)
    


# num1=5
# num2=11
# count=0
# for i in range(num1,num2+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         # print(i)
#         count+=1
        
# print(count)


# num1=100
# num2=1000

# for i in range(num1,num2):
#     sum=0
#     for j in str(i):
#         sum+=int(j)**len(str(i))
#     if i==sum:
#         print(i)

# while num1<num2:
#     temp=num1
#     sum=0
#     count=0
#     while num1>0:
#         count+=1
#         num1//=10
#     num1=temp 
#     while temp>0:
#         sum+=(temp%10)**count
#         temp//=10
#     if num1==sum:
#         print(sum)
#     num1+=1

num1=10
num2=25

# while num1<num2:
#     i=2
#     count=0
#     while i<num1:
#         if num1%i==0:
#             count+=1
#         i+=1
#     if count==0:
#         print(num1)
#         break
#     num1+=1


# while num2>=num1:
#     count=0
#     i=2
#     while i<num2:
#         if num2%i==0:
#             count+=1
#         i+=1
#     if count==0:
#         print(num2)
    
#     num2-=1

# name = "Krishna"
# vowels=''
# for i in name:
#     if i in 'aeiou':
#         vowels+=i
# print(vowels[-1])

# n = 10

# for i in range(1, n+1):
#     if i % 2 != 0:   # if odd
#         continue     # skip this iteration
#     print(i, end=" ")

# def sum(a):
#     if a%2==0:
#         return True
#     return False
# print(sum(5))

# def year(num):
#     if (num%4==0 and num%100!=0) or (num%400==0):
#         return True
#     return False
# print(year(2004))

# def prime(num):
#     if num<2:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(prime(9))

# def check(num1):
#     for i in range(num1,num1+1):
#         temp=i
#         sum=0
#         while temp>0:
#             sum+=(temp%10)**len(str(i))
#             temp//=10
#         if i==sum:
#             return sum

# for i in range(100,1000):
#     if check(i):
#         print(check(i))

# factorial

# def fact(num):
#     factorial=1
#     if num==0:
#         return factorial*1
#     else:
#         factorial=factorial*num*fact(num-1)
#     return factorial
# print(fact(5))

# def rev(num,num2=0):
#     if num==0:
#         return num2
#     else:
#         a=num%10
#         num2=num*10+a
#         return rev(num//10,num2)

# print(rev(1234))

# def reverse_number(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_number(n // 10, rev * 10 + n % 10)

# print(reverse_number(12345))   # 54321

