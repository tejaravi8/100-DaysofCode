# while reverse------------------------------------------------------------------------

name="teja"
count=len(name)
rev=""
while 0<count:
    rev=rev+name[count-1]
    count-=1
print(rev)