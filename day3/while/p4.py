# count using while----------------------------------------------------------------

num=9948
count=0
while num>0:
    count+=num%10
    num=num//10
print(count)
