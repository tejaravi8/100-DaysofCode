#  Count how many times digit 7 appears between 1 to 100.
count=0
for i in range(1,100):
    if "7" in str(i):
        count+=1    
print(count)