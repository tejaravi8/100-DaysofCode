# Combine two lists into a dictionary using zip().

w=[1,2,3]
n=[4,5,6]
freq={}
for i,j in zip(w,n):
    freq[i]=j
print(freq)
