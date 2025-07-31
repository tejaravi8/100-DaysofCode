# 10. Use a while loop to print all prime numbers between 50 and 100. 

i=50
while i<=100:
    j=1
    count=0
    while j<i+1:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print(i)
    i+=1
    
          