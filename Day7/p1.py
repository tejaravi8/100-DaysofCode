# 1. Compress a string using character counts. 
# Input: "aabbbcc" → Output: "a2b3c2" 

t="aabbbcc"
count=1
result=""
for i in range(1,len(t)):
    if t[i]==t[i-1]:
        count+=1
    else:
        result+=t[i-1]+str(count)
        count=1
result+=t[-1]+str(count)
print(result)

    