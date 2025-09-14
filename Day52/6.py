# # # nums=[1,2,3,4]
# # # nums.reverse()
# # # print(nums)

# # # nums=[1, 2, 3,2,9,5,8]
# # # # print(nums[::-1


# # # print(sorted(nums),reversed(nums))
# # # print(nums)
# # # # nums.sort()
# # # # print(nums)

# # # n1=[1,2,3,4,5]
# # # n2=[1,2,6,8,9]

# # # for i in n1:
# # #     if n1[0]==i:


# # # lock=True
# # # while lock:
# # #     names=input('enter password:')
# # #     upper=0
# # #     lower=0
# # #     spcl=0
# # #     digit=0

# # #     for i in names:
# # #         if i.isupper():
# # #             upper+=1
# # #         elif i.islower():
# # #             lower+=1
# # #         elif i.isdigit():
# # #             digit+=1
# # #         else:
# # #             spcl+=1

# # #     if upper>=1 and lower>1 and spcl>=1 and digit>=1 and len(names)>8:
# # #             print('strong password')
# # #             lock=False
# # #     elif upper>=1 and lower>1 and spcl>=1 and digit>=1 and len(names)<8:
# # #             print('enter some to make strong')
            
# # #     else:
# # #             print('week password')

# # # names='aabbcc'
# # # new=''
# # # for i in names:
# # #     if i not in new:
# # #         new+=i
# # #     else:
# # #         print(i,end=' ')
        
# # # print(new,end=' ')

# # # name='123'
# # # new=''
# # # for i in name:
# # #     new+=chr(ord(i)+1)
# # # print(new)

# # # name='he llo wor ld'
# # # new=''
# # # for i in name:
# # #     if i!=' ':
# # #         new+=i
# # # print(new)

# # # name='he llo'
# # # rev=''
# # # for i in range(len(name)-1,-1,-1):
# # #     if name[i]!=' ':
# # #         rev+=name[i]
# # # print(rev)

# # # name='Rav*IteJa'
# # # new=''
# # # for i in name:
# # #     if 65<=ord(i)<=90:
# # #         new+=chr(ord(i)+32)
# # #     elif 97<=ord(i)<=122:
# # #         new+=chr(ord(i)-32)
# # #     else:
# # #         new+=i
# # # print(new)

# # # nums=[5, 5, 5, 5, 5]
# # # responce=None
# # # for i in nums:
# # #     if i==nums[0]:
# # #         responce=True
# # #     else:
# # #         responce=False
# # #         break
# # # if responce:
# # #     print('yes')
# # # else:
# # #     print('no')
        
        

# # # first=second=float('inf')
# # # for i in nums:
# # #     if i<first:
# # #         second=first
# # #         first=i
# # #     elif first<i<second:
# # #         second=i
# # # print(second)
        
# # def flatten(name):
# #     new=[]
# #     def check(nums):
# #         for i in nums:
# #             if type(i)==list:
# #                 check(i)
# #             else:
# #                 new.append(i)
# #     check(name)
# #     return new
# # a=flatten([[1, 2], [3, 4]])

# # m=[]
# # if len(m)==0:
# #     print(True)
# # else:
# #     print(False)

# nums=[1, 2, 3, 4, 5, 6]
# # pedda=[]
# # new=[]
# # c=0
# # for i in nums:
# #     if c<2:
# #         new+=[i]
# #         # print(new)
# #         c+=1
# #     else:
# #         pedda+=[new]
# #         c=1
# #         new=[i]
# # pedda+=[new]
# # print(pedda)

# # for i in nums:
# #     if i==2:
# #         print('found')
# #         break

# k=2
# new=nums[-k:]+nums[:len(nums)-k]
# print(new)

# n=[1,2,3,4,1,2,3,1,2,5,6]
# m=[]
# for i in n:
#     if i not in m:
#         m.append(i)
        
# print(n)
# print(m)