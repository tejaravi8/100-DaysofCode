# # decorator

# def items(printer):
#     def inner():
#         print("A4,ink")
#     printer()
#     return inner
    
    
# # @items
# # def printer():
# #     print("printing...")
# # printer()
# # n=input("enter values:")
# # file=open("text.txt","w")
# # file.write(n)

# res=open('teja.jpg','rb')
# new=open('teja2.jpg','wb')

# data=res.read()
# print(new.write(data))

# res=open('text.txt','r')
# data=res.readlines()
# print(data)

# res1=[f"Line{i}:\n" for i in range(20)]

# res=open('text.txt','w')
# res.writelines(res1)



# 'teja'
# print("teja")

# file=open("text.txt",'r')
# data=file.read()
# print(data)

# file=open("text.txt",'a')
# file.write("i want to add new lines\n")
# file.close()

# file=open("teja.txt",'a')
# # file.write("hello every one\n")
# # file.write('tejaa learning file handling')
# file.write("extra lins means more size")
# # data=file.read()
# # print(data)
# file.close()


# name=input("enetr your name:")
# roll=input("enter roll:")
# marks=input("enter marks:")

# with open('text.txt','r') as nam:
#     for detail in nam:
#         name, roll, mark=detail.strip().split(",")
#         print(f"Name: {name}, Roll: {roll}, Marks: {mark}")




# i=123
# sum=0
# while i>0:
#     sum+=(i%10)**2
#     i//=10
# print(sum)
    
    
# i=1
# while i<=30:
#     if i%3==0 or i%5==0:
#         i+=1
#         continue
#     print(i)  
#     i+=1


# n = 101
# while True:
#     temp = n
#     digit_sum = 0
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10
#     if digit_sum % 7 == 0:
#         print("Found:", n)
#         break
#     n += 1


# name="my name is teja"   #aj etsi em anmy

# ref=""
# r=""
# rev=""
# for i in range(0,len(name)):
#     if name[i] != " ":
#         ref+=name[i]
#         # print(ref)
#     else:
#         rev=name[len(name)-i:-(len(ref)+(i-1)):-1]
#         r+=rev
#         rev=""
#         ref=""
# print(r)

# rev=name[1:4:]
# print(rev)


# delete
# import os

# if os.path.exists("new_.txt"):
#     os.remove('new_.txt')
# else:
#     print("file does not exist")


# folder empty

# import os

# if os.path.exists("folder"):
#     os.rmdir('folder')
# else:
#     print("file does not exist")
    
# (non empty)folder delete 
   
# import os
# import shutil 
# if os.path.exists("fold"):
#     shutil.rmtree('fold')
# else:
#     print("file does not exist")



# # csv

import csv

