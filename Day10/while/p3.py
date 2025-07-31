# 3. Use a while loop to count the number of digits in a given number.

num=123456
count=0
while num>0:
    count+=1
    num=num//10
print(count)