# Write a function to check if a number is prime.

def prime(a):
    num=a
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not a prime")
prime(5)