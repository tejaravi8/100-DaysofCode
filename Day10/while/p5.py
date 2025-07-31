#  Use a while loop to repeatedly sum the digits of a number until it becomes a single digit.

num=12345
sum=0
while num>9:
    sum+=num%10
    num=num//10
    
print(sum)