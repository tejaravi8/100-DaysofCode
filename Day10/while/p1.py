# 1. Write a program using a while loop to check if a number is a palindrome. 

num=12321
original=num
rev=0

while num>0:
    
    rev=num%10+rev*10
    
    num=num//10


if original==rev:print("palindrome",original)
else:print('pal',rev)