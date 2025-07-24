# Check if a number is a palindrome using while loop.

num=41863
rev=0

while 0<num:
    rev=num%10+rev*10
    num=num//10
if num==rev :print("palindrome") 
else:print("not a palindrome")