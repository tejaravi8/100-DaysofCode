# # # n=[121,132,143,151,101]
# # # new=[]
# # # l=len(n)
# # # while l>0:
# # #     num=n[l-1]
# # #     temp=num
# # #     rev=0
# # #     while temp>0:
# # #         rev=temp%10+rev*10
# # #         temp//=10
# # #     if rev==num:
# # #         new+=[rev]
# # #     l-=1
# # # print(new)

# # n=[121,371,143,153,101]
# # new=[]
# # l=len(n)
# # while l>0:
# #     num=n[l-1]
# #     s=0
# #     c=0
# #     temp=num
# #     while temp>0:
# #         c+=1
# #         temp//=10
# #     temp=num
# #     while temp>0:
# #         s+=(temp%10)**c
# #         temp//=10
# #     if num==s:
# #         new+=[s]
# #     l-=1
# # print(new)

# # name='ravibteja'
# # l=len(name)
# # if l%2!=0:
# #     for i in range(int(l/2)+1):
# #         print(name[i],name[l-1-i])
# # else:
# #     for i in range(int(l/2)):
# #         print(name[i],name[l-1-i])

# # name='ravibteja'
# # i=0
# # r=len(name)-1

# # while i<=r:
    
# #     if i==r:
# #         print(name[i])
# #     else:
# #         print(name[i],name[r])
    
# #     i+=1
# #     r-=1



# #* * * * *
# #* * * * *
# #*   * * *
# #*     * *
# #* * * * *
# n=5
# a=0
# for i in range(n):
#     if i<n//2 or i==n-1:
#         print('* '*n)
#     else:
#         print('*  '+"  "*(a),"* "*(n-i))
#         a+=1

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev = 0
    
    for ch in reversed(s):  # Start from right
        value = roman[ch]
        if value < prev:
            total -= value   # subtract case
        else:
            total += value   # normal addition
        prev = value
    return total

# Example
print(roman_to_int("IX"))    # 9
print(roman_to_int("LVIII")) # 58
print(roman_to_int("MCMXCIV")) # 1994
