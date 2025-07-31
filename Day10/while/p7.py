# 7. Create a while loop to check whether a number is an Armstrong number. 

num=153
check=num
sum=0
while num>0:
    sum+=(num%10)**3
    num=num//10
if sum==check:
    print("armstrong number")
else:
    print("not an armstrong")