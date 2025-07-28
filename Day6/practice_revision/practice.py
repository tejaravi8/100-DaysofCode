# l=["teja","yy","kk"]
# for i,j in enumerate(l):
#     print(i,j)
q=[1,2]
a=list(tuple( (lambda x,y : x+y,q)))
print(tuple(a))