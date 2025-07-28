# Print all prime numbers from a list. 

a=[2,3,4,5,6,7,8,221]

for i in range(len(a)):
    for j in range(2,len(a)):
        if a[i]%j==0:
            break
        else:
            print(a[i])
            break
