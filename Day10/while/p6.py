# 6. Use a while loop to find the sum of factorials from 1 to n.

n=5
i=1
sum=0
while i<=n:
    factor=1
    j=1
    while j<=i:
        factor=factor*j
        j+=1
    sum+=factor
    i+=1
    
print(sum)