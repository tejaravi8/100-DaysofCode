# 11.  Count number of vowels in a string using while.

# a=list("raviteja")
# print(a)
# v=['a','e','i','o','u']
# # a=list(a)
# count=0

# while len(a)>0:
#     for i in a:
#         if i in v:
#             count+=1
#         a.remove(i)
# print(count)
# 
a="raviteja"
i=0
vowel_count=0
while i< len(a):
    if a[i].lower() in "aeiou":
        vowel_count+=1
    i+=1
print(vowel_count)
    
