# 2. Use a while loop to reverse a number (e.g., 123 → 321).

i=123
rev=0
while i>0:
    rev=i%10+rev*10
    
    i=i//10
    
print(rev)