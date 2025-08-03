number series

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
alphabets pattern

  
i=65
while i<=70:
    j=65
    while j<=i:
        print(chr(j),end=" ")
        j+=1
    print()
    i+=1


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

6.Bus Ticket Counter Simulation:
          Keep booking tickets until seats are 0.

tickets=52

while tickets>=1:
    
    book=input('Enter "Book Ticket" for booking : ')
    if book=="Book Ticket":
        tickets-=1
        print(f"Booking Successful, Remaining tickets : {tickets}")
    else:
        print("Booking Unsuccessful, Enter valid")

print("Tickets Over")
        

