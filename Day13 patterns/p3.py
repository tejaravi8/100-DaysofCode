# alphabet non repetion

i=64                # ord('A')-1
row=1
while row<=4:       #1 , 2 , 3 , 4 , 5
    j=1
    print(f"row:{row}", end="  ")
    
    while j<=row:
        print(chr(i+j),end=" ")
        j+=1
    print()
    i+=row
    row+=1