# 4. Generate the Fibonacci series up to a given number using a while loop.

i=0
j=1
print(i,j)
num=1

while num<=10:
    
    i,j=j,i+j
    print(i,j)
    
    num+=1