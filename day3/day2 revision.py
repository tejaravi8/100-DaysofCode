nums=[1,2,5,3,6,1,6,9,0,8,6]
second=first=0
for i in nums:
    if i>first:
        second=first
        first=i
    elif second<i and i<=first:
        second=i
print(second)
print(first)

a=set(nums)
print(a)
print(min(a))

n=max(nums)
nums.remove(n)
max2=max(nums)
print(max2)
# -----------------------------------------------------------------------------------


list1=["roll1","roll2","roll3","roll4","roll5"]
list2=["teja","sai","vanaja","karthik","prasad"]

freq={}
for i,j in zip(list1,list2):
    if j not in freq:
        freq[i]=j
        
print(freq)

# -----------------------------------------------------------------------------------


list1=[1,2,3]
list2=[1,2,7]
# new=[]
for i,j in zip(list1,list2):
    if i==j:
        print("equal",i)
    else:
        print("not equal",i,j)
    new.append(i+j)
print(new)


# -----------------------------------------------------------------------------------


list1=[(1,2),(3,4),(5,6)]
a,b=zip(*list1)
print(list(a))


# -----------------------------------------------------------------------------------




num=5555
count=0
while 0<num:
    count+=1
    num=num//10
print(count)

name="teja"
a = [1, 2, 3]
b = ['a', 'b', 'c']

result = tuple(zip(a, b))
print("Zipped List:", result)

x, y = zip(*result)
print("Unzipped:", list(x), list(y))




    
#-------------------------------------------------------------------------------------




    
rows=4
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print("")
    
rows = 4
for i in range(1, rows + 1):
    print(' ' * (rows - i), end='')
    print('* ' * i)


rows = 4
ch = 65  # ASCII of 'A'
for i in range(1, rows + 1):
    print((chr(ch) + ' ') * i)
    ch += 1



 # listt=[10,15,20]

# # res=[]
# # for i in listt:
# #     r=[]
# #     for j in range(1,i):
# #         if i%j==0:
# #             r.append(j)
# #     res.append(r)
             
# # print(res)
# listt=[10,15,20]
# res={}
# for i in listt:
#     r=[]
#     for j in range(1,i):
#         if i%j==0:
#             r.append(j)
#     res[i]=r
# print(res)



# rows=4
# ch=65
# for i in range(1,rows+1):
#     for j in range(i):
#         print(chr(ch)+" " , end=" ")
#     print()    
#     ch+=1


# rows = 4
# ch = 65  # ASCII of 'A'
# for i in range(1, rows + 1):
#     print((chr(ch) + ' ') * i)
#     ch += 1
