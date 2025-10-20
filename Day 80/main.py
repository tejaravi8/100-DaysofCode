# # m=[]
# # def flat(n):
# #     for i in n:
# #         if type(i)==list:
# #             flat(i)
# #         else:
# #             m.append(i)
# # flat([1, [2, 3], [4, 5], 6] )
# # print(m)

# # a=[1, 2, 3, 2, 4, 1, 5]
# # ele=5
# # for i in range(len(a)):
# #     if i==ele:
# #         print(i)

# # a=['apple', 'banana', 'apple', 'mango', 'banana', 'apple']
# # f={}
# # for i in a:
# #     if i not in f:
# #         f[i]=1
# #     else:
# #         f[i]+=1
# # print(f)
# a=[12, 45, 23, 67, 34]
# first=second=-float("inf")
# f=s=float("inf")
# for i in a:
#     if i>first:
#         second=first
#         first=i
#     elif first>i>second:
#         second=i

#     if i<f:
#         s=f
#         f=i
#     elif f<i<s:
#         s=i

# print(s,second)
# a=[1, 2, 3, 4, 5]
# new=[]
# for i in range(len(a)-1,-1,-1):
#     new.append(a[i])
# print(new)

# a=["Ravi", "Sita", "Arjun", "Kavitha"]
# l=''
# j=0
# for i in a:
#     c=0
#     for h in i:
#         c+=1
#     if c>j:
#         j=c
#         l=i
# print(l)
# a=[1, 5, 2, 2, 3, 7,5]
# g=[]
# dif=2
# for i in a:
#     for j in a:
#         if i-j==dif:
#             # p=(i,j)
#             # if p not in g:
#             g.append((i,j))
# print(g)
# a=[1, 2, 3, 4, 9, 16, 20]
# for i in a:
#     if int(i**(0.5))==i**(0.5):
#         print(i)

# a = [1, 2, 3, 4, 9, 16, 20]
# # perfect_squares = []

# for num in a:
#     i = 1
#     while i * i <= num:
#         if i * i == num:
#             print(num)
#             break
#         i += 1

# print("Perfect squares:", perfect_squares)

# a=[0, 1, 0, 3, 12]
# a1=[]
# zero=0
# for i in a:
#     if i!=0:
#         a1.append(i)
#     else:
#         zero+=1
# for i in range(zero):
#     a1.append(0)
# print(a1)
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# for i in list1:
#     if i not in list2:
#         print(i)
# f=0
# for i in a:
#     if i==0:
#         a1.append(i)
#     else:
#         a1.insert(f,i)
#         f+=1
# print(a1)

# a=[1, 2, 3, 7, 8, 9,1]
# s=10
# f=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==s:
#             p=(a[i],a[j])
#             if p not in f and (a[j],a[i]) not in f:
#                 f.append(p)

# print(f)
# a=[1, 2, 3, 4, 5, 6]
# # s=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         for k in range(j+1,len(a)):
#             if a[i]+a[j]+a[k]==10:
#                 print((a[i],a[j],a[k]))

# print(s)

# a=[[1, 4, 7], [2, 5, 8], [3, 3, 6]]
# new=[]
# for i in a:
#     for j in i:
#         new.append(j)
# print(new)

# for k in range(len(new)):
#     for j in range(k+1,len(new)):
#         if new[k]>new[j]:
#             new[k],new[j]=new[j],new[k]
#         else:
#             new[k],new[j]=new[k],new[j]
# print(new)

# a = [3, 4, -7, 1, 3, -1, 2, -2]

# for start in range(len(a)):
#     x = 0
#     s = []
#     for i in range(start, len(a)):
#         x += a[i]
#         s.append(a[i])
#         if x == 0:
#             print(s)


# def longest_increasing_subsequence(arr):
#     n = len(arr)
#     lis = [1] * n  # Each element is at least a subsequence of length 1

#     for i in range(1, n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 lis[i] = max(lis[i], lis[j] + 1)

#     return lis

# # Example
# arr =[10, 2, 5, 3, 7, 101, 18]
# l=0
# a=0
# for i in arr:
#     if i>a:
#         a=i
#         l+=1
# print(l)

# print("Length of LIS:", longest_increasing_subsequence(arr))


# name="my name is ravi tejesh"
# l=[]
# k=''
# for i in range(0,len(name)):
#     if name[i-1]==" ":
#         l.append(k)
#         k=''
#         k+=name[i]
#     else:
#         k+=name[i]
# l.append(k)
# print(l)

# d=["kathyayani","nalliakhil","daddy"]
# l=""
# for i in d:
#     if len(i)>len(l):
#         l=i
# print(l)

#insertion sort





a=[5,2,3,1]
for i in range(1,len(a)):
    key=a[i]
    j=i-1
    while (j>=0 and a[j]>key):
        a[j+1]=a[j]
        j-=1
    a[j+1]=key
print(a)