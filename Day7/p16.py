# Write Function to check if a list is sorted or not. 
f=[1,2,3,4]
is_sorted=True
for i in range(len(f)-1):
    if f[i]>f[i+1]:
        is_sorted=False
        break
        
print(is_sorted)