# 8.	words = ["level", "python", "madam", "world", "racecar"] print palindrome words 
 
words = ["level", "python", "madam", "world", "racecar"]
            
# res=["pali" if i[::-1]==i else "not" for i in words]

res=[i for i in words if i[::-1]==i]
print(res)
