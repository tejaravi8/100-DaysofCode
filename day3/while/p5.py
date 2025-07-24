num=256
res=0
while 0<num:
    res=res*10+num%10
    num=num//10
    
print(res)