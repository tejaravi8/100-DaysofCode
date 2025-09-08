# def check(num):
#     new=0
#     for i in str(num):
#         new+=(int(i)**3)
        
#     if num==new:
#         return True


# for i in range(1,501):
#     if check(i):
#         print(i)

i=1
while i<=500:
    num=i
    a=num
    new=0
    while num>0:
        new+=(num%10)**(3)
        num//=10
    if new==a:
        print(new)
    i+=1


# for i in range(2,100):
#     if i%2==0:
#         print(i)
#         continue
    
num=198
new=0
while num>0:
    new=num%10
    num//=10
    break

print(num)