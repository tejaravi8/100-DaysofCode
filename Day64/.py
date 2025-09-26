# # # # # n=5
# # # # # for i in range(1,n+1):
# # # # #     for j in range(i,n+1):
# # # # #         print(' ',end=" ")
# # # # #     for j in range(1,i+1):
# # # # #         print('*',end=' ')
# # # # #     for j in range(1,i):
# # # # #         print('*',end=' ')
# # # # #     print()
# # # # # print()

# # # # # *
# # # # # * *
# # # # # *   *
# # # # # *     *
# # # # # * * * * *

# # # # # n=10
# # # # # for i in range(1,n+1):
# # # # #     if i==1 or i==10 or i==2:
# # # # #         print('* '*i)
# # # # #     else:
# # # # #         print('* '+'  '*(i-2)+'* ')

# # # # # n=5
# # # # # for j in range(1,n):
# # # # #         if j==1 or j==5 or j==2:
# # # # #             print('* '*j)
# # # # #         else:
# # # # #             print('* '+'  '*(j-2)+'* ')
# # # # # for j in range(n,0,-1):
# # # # #         if j==1 or j==2:
# # # # #             print('* '*j)
# # # # #         else:
# # # # #             print('* '+'  '*(j-2)+'* ')


# # # # # s = "maffam"
# # # # # rev=0
# # # # # i=0
# # # # # l=len(s)-1
# # # # # while l>=i:
# # # # #     if s[i]!=s[l]:
# # # # #         print('not a pal')
# # # # #         break
# # # # #     i+=1
# # # # #     l-=1
# # # # # else:
# # # # #     print('pal')


# # # # for i in range(len(s)-1,-1,-1):
# # # #     rev+=s[i]
# # # # print(rev)

# # # # name='teja'
# # # # name='T'+name[1:]
# # # # del name
# # # # print(name)

# # # # s = "geeksforGeeks"
# # # # # s = "G" + s[1:]   # create new string
# # # # # del s
# # # # s='hello teja'
# # # # s.replace('hello','how r u')
# # # # s1=s.replace('hello','how r u')
# # # # print(s1)

# # # name=' hello '
# # # print(len(name.strip()))
# # # print(name)
# # # print(len(name))

# # s='teja is goodboy '
# # print(s.replace('teja','pablo'))
# # print(s*3)


# a = 'longer'
# b = 'There'


# # short=min(len(a),len(b))
# # longer=''
# # if short==len(a):
# #     short=a
# #     longer=b
# # else:
# #     short=b
# #     longer=a

# # print(short,longer)


# def findPattern(s,p):
#     #code here
#     l=0
#     s=s
#     p=p
#     for i in range(len(s)):
#         if s[i]==p[l] and (p.lower() in s.lower()):
#             return i
#             break
#     else:
#         return -1
# print(findPattern(s = "World",p = "Doodle"))

# s = "i.like.this.program.very.much".split('.')
# print(s)
# new=''
# for i in reversed(s):
#     new=new+i+'.'

# print(new[:len(new)-1])
# # print(s)
# def reverseWords(s):
#         s=s.split('.')
#         print(s)
#         new=''
#         for i in reversed(s):
#             if i!="":
#                 new=new+i+'.'
#         return new[:len(new)-1]
# print(reverseWords(s=".i.like.this.program.very.much."))

d={
    "I":1,
    "V":5,
    "X":10
}
input='IX'
s=0
for i in range(0,len(input)):
    # print(d[input[i]])
    if input[i-1]=='I':
        s+=d[(input[i])]-2
    else:
        s+=d[(input[i])]
print(s)