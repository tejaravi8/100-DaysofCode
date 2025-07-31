# 9. Use a while loop to find the largest digit in a given number. 

max=0
num=25336
while num>0:
    x=num%10
    if x > max:
        max=x
    num=num//10
print(max)
        