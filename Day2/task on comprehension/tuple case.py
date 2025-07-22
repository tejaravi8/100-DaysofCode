# 3.	 From a list of names, create a tuple of names that start with the letter 'A' or 'a' 

res=tuple(i for i in ['Apple',"Ajay","avunu","Babu","papa"] if i[0]=="a" or i[0]=="A")
print(res)

# tup=[]
# for i in names:
#     if i[0]=="a" or i[0]=="A":
#         tup.append(i)
# print(tuple(tup))