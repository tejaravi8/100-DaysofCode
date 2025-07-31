import random 

# data=random.randint(1,2)
i=True
count=0
while i:
    data=random.randint(1,2)
    count+=1
    if data==2:
        print('2 fount',count)
        break
    i=True