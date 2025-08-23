# Print a pattern using *.

# for i in range(0,6):
#     print(i*'*')

# n=5
# for i in range(1,n+1):
#     spaces=(n-i)*" "
#     stars='*'*(2*i-1)
#     print(spaces+stars)



n=int(input('enter the num:- '))
count=0
for i in range(1,n):
    if n%i==0:
        count+=1
if count==2:
    print(i)







