n=5
res=[]
for x in range(1,100):
    for j in range(2,x):
        if x%j==0:
            break
    else:
        res.append(x)
    if len(res)==n:
        print(res)
        break
    
def prime():
    n=input("enter number:")
    if n<1:
        print("false")
        