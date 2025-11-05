# file=open("text2.txt","a")
# file.write("\nHello babu")
# file.close()
# # print(content)

# with open("teja.txt","r") as file:
#     doc=file.tell()
#     print(doc)

# with open("notes.txt","r") as file:
#     # file.write("Python file handling is easy!")
#     data=file.read()
#     with open("new.txt","w") as fi:
#         fi.write(data)
#     # for i in range(len(data)):
#     #     # print(data[i],i+1)
#     # # c=file.read()
#     # # print(c)

# with open("numbers.txt","r") as file:
#     # file.write("\nhello hemanth love got job")
#     a=file.read()
#     print(a)

# with open("numbers.txt", "r") as file:
#     for line in file:
#         print(line.upper().strip())

# with open("numbers.txt","w") as file:
#     for i in range(1,11):
#         file.write(str(i)+" \n")

# with open("numbers.txt","r") as file:
#     for i in file:
#         if (bool(int(i.strip())%2=1))==True:
#             print(i.strip())
    
# import os

# os.remove("numbers.txt")
# os.remove("notes.txt")

# with open("while.txt","w") as file:
#     while True:
#         ask=input("enter something ... enetr break for end>>>:smile😁")
#         if ask.strip()=="break":
#             break
#         file.write(ask+"\n")

# with open("while.txt","r") as file:
#     for i in file:
#         with open("greet.txt","a") as fi:
#             fi.write("hello"+" "+i.strip()+"\n")

# with open("numbers.txt","r") as file:
#     number=0
#     name=""
#     for i in file:
#         a,b=i.split()
#         # print(type(int(b)))
#         num=int(b)
#         if int(b)>number:
#             number=num
#             name=a
#     print(number,name)
            
        
# (a,b)=[1,2]
# print(b)

# with open("numbers.txt","r") as file:
#     fil=file.readlines()
#     # print(fil)
#     for i in reversed(fil):
#         with open("reversed.txt","a") as f:
#             f.write(i.strip()+"\n")

# with open("data.txt", "r") as f:
#     lines = f.readlines()

# with open("reverse.txt", "w") as f:
#     for line in reversed(lines):
#         f.write(line)

# with open("while.txt","r") as p:
    
    # data=p.read()
    # # print(type(data))
    # data=data.replace("teja","pablo")
    # # for i in data:
    # with open("relace.txt","w") as ne:
    #     ne.write(data)


with open("relace.txt", "r") as f1, open("reversed.txt", "r") as f2, open("combined.txt", "w") as out:
    out.write(f1.read() + "\n" + f2.read())
        