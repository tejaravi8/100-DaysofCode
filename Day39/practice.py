# Check if two strings are anagrams.

# Find the first non-repeating character in a string.


# Count vowels and consonants in a string.
# name=""
# vowels=0
# cons=0
# for i in name:
#     if i in 'aeiou':
#         vowels+=1
#     else:
#         cons+=1
# print(vowels,cons)
        
        
# Remove duplicate characters from a string.

# Check if a string is palindrome (without slicing).

# Find the most frequent character in a string.
# name='raavitejaa'
# char=''
# # print(len(long))
# for i in range(len(name)):
#     count=0
#     for j in range(len(name)):
#         if name[i]==name[j]:
#             count+=1
#     if count==1:
#         char=name[i]
#         break
        
# print(char)
    
# Reverse each word in a sentence.
# name="Reverse each word in a sentence"
# new=[]
# name2=''
# for i in range(1,len(name)):
#     if name[i-1]!=' ':
#         name2+=name[i-1]
#     else:
#         new+=[name2]
#         name2=''
# new+=[name2+name[-1]]
# name2=''   

# for i in range(len(new)-1,-1,-1):
#     name2+=new[i]+' '
# print(name2)
    
# Capitalize the first letter of each word (without .title()).
# name='good afternoon everybody'
# new=''
# for i in range(1,len(name)):
#     if name[i-1]==" ":
#         new+=name[i].upper()
#     else:
#         new+=name[i]
# print(name[0].upper()+new)


# Replace spaces with - in a string.
# name="Replace spaces with - in a string"
# new=''
# for i in name:
#     if i==' ':
#         new+='-'
#     else:
#         new+=i
# print(new)
# # Compress a string like "aaabbc" → "a3b2c1".

name='aaabbc'
count=1
new_name=''
for i in range(1,len(name)):
    if name[i-1]==name[i]:
       count+=1
    else:
        new_name+=name[i-1]+f'{count}'
        count=1
new_name+=name[-1]+f'{count}'       
print(new_name)





























# name="rraviiteja"
# for i in range(len(name)):
#     count=0
#     for j in range(len(name)):
#         if name[i]==name[j]:
#             count+=1
#     if count==1:
#         print(name[i])
#         break
    
    