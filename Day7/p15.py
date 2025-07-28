#  Replace all negative numbers in a list with 0. Using list comprehention? 
a=[1,-1,4,-2]
r=[0 if i<0 else i for i in a]

print(r)