# 6.Bus Ticket Counter Simulation:
#           Keep booking tickets until seats are 0.

tickets=5

while tickets>=1:
    
    book=input('Enter "Book Ticket" for booking : ')
    if book=="Book Ticket":
        tickets-=1
        print(f"Booking Successful, Remaining tickets : {tickets}")
    else:
        print("Booking Unsuccessful, Enter valid")

print("Tickets Over")

        

