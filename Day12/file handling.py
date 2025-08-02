# # # file=open("teja.txt","a")
# # # file.write("hi 51rfrnds\n")
# # # # print(file.read())
# # # file.close()

# # # print("\ndone")

# # with open("teja.txt","r") as file:
# #     data=file.read()
# #     print(data)
# #     print("\n done")


# # # def log_user_activity(username):
# # #     with open('user_log.txt', 'a') as file:
# # #         file.write(f"User {username} logged in.\n")

# # # # Usage
# # # log_user_activity('teja')


# # with open("pablo.txt","a") as file:
# #     file.write("\nExtra Extra Large")

# ## read one line using readline()

# # with open("pablo.txt","r") as p:
    
# #     line=p.readline()
# #     print(line)

# # 4. Read all lines using readlines()

# # with open("pablo.txt","r") as p:
# #     lines=p.readlines()
# #     print(lines[0:len(lines)-1])
    
    
# # file=open("chandu.txt","r")
# # lines=file.readlines()
# # print(lines[0:len(lines)])
# # file.close()

# # with open("chandu.txt",'r') as c:
# #     print(c.read())

# # lines=["\nteja is my name","\nchandu is my brother"]
# # with open("chandu.txt",'a') as file:
# #     file.writelines(lines)

# # copy

# # with open("chandu.txt","r") as t:
# #     with open("new_c.txt","w") as teja:
# #         teja.write(t.read())

# # t=open("chandu.txt","r")
# # c=open("nEw.txt","w")
# # data=c.write(t.read())
# # print(data)
# # c.close()
# # t.close()

# # t=open("teja.jpg","rb")
# # data=t.read()
# # e=open("sai.jpg","wb")
# # p=e.write(data)
# # print(data)


# What is file handling in Python?

# file handling is the process of creating , reading , writing, and deleting files using python code. it allows a programm to store and manage data perminantly


# 2.	Difference between read(), readline(), and readlines().

# read(): read specified size of data  upto 300lines ala
# readline():  read one line   in str
# readlines(): read all lines in list

# 3.	What are different file modes in Python?

# 'x'- to create we use x Mode
# 'w'- to create and write in a file we use write(w) Mode
# 'r' - to read a existing file we use  read(r) mode
# 'a'- to add and create new file we can use append (a) mode

# 4.	How do you copy content from one file to another?
# by reading data in first file we store data in a variable
# later we have to write on new file with existing variable

# 5.	Write code to read and write a text file.

# 6.	Find the sum and average of elements in a list.

# a=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# # avg=0
# for i in a:
#     sum+=i
# avg=sum/len(a)
# print(sum)
# print(avg)

# 7.	Remove all elements from a list that appear more than once.

# 8.	Convert a tuple of tuples to a dictionary:
# Example: ((1, 'a'), (2, 'b')) → {1: 'a', 2: 'b'}

# 9.	Write a Python program to delete a file named data.txt


# with open("new_.txt",'a') as p:
#     p.write('hello babu\n \nhello papa')

import os

if os.path.exists("teja.txt"):
    os.remove('teja.txt')
else:
    print('does not exist')
