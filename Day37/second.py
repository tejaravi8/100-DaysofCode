# from encapsulation import car

# class speedcar(car):
    
    
#     def color(self,attre):
#         return attre
    
#     def brand(self,attribute2):
#         return attribute2
    
# car1=speedcar()
# print(car1.color('red'))
# print(car1.brand("bmw"))


# from ss import teja

# obj1=teja()
# obj1.sex("female")

# String comprehension 
# I/p - aabccca 
# O/p - a2b1c3a1

# word="aabccca"
# new=""
# count=1
# for i in range(1,len(word)):
#     if word[i-1]==word[i]:
#         count+=1
#     else:
#         new+=word[i-1]+str(count)
#         count=1
        
# new+=word[-1]+str(count)

# print(new)

# Output the number of vowels in your name only if it equals to the given input 
# I/p - 2
# Name = Rama
# O/p - a2

# num=2
# name='ramaaii'
# new=''
# for i in name:
#     if i in 'aeiou':
#         new+=i

# count=1
# n=''
# # new=''
# for i in 'aeiou':
#     if i in new and count<=2:
#         count+=1
        
#     elif count==new:
#         n+=i+str(count)
#         count=1
# print(n)

# num=2
# name='rama'
# dict={}
# for i in name:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# # print(dict)
# for i,j in dict.items():
#     if i in 'aeiou':
#         if j==num:
#             print(i+str(j))


# Write an example for polymorphism in real time using USECASE

# class grandfather:
    
#     def gender(self,sex):
#         self.sex=sex
#         print(self.sex)
    
# class father(grandfather):
    
#     def gender(self,sex):
#         self.sex=sex
#         print(self.sex)
        
# obj=father()
# obj2=grandfather()
# obj2.gender('maleeee')
# # obj.gender('male')
        

# . Insert number of nested arrays with number of elements given by the user as input 
# I/p - 2
# O/p - [[x,y],[x,y]]
# num=2
# new=[]
# a='ab'
# for i in range(num):
#     sub=[]
#     for j in a:
#         sub+=[j]

#     new+=[sub]
# print(new)

name='the match was exiting'
new=[]
name2=''
for i in range(1,len(name)):
    if name[i-1]==' ':
        new+=[name2]
        name2=''
    else:
        name2+=name[i-1]
        
new+=[name2+name[-1]]

print(new)
        
# name2=''
# for i in name:
#     if i !=' ':
#         name2+=i
#     else:
#         new+=[name2]
#         name2=i

# print(new)