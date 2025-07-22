# two players game
import random
p1=p2=0
a=random.randint(1,100)
for i in range(5):
    print(f"===== {i} round=== ")
    if p1<=a and p2<=a :
        p1+=int(input("enter value P1:"))
        if p2>=a:
            print("p2 win 9",a)
            break    
        elif p1>=a:
            print("p1 win",a)
            break

    for j in range(1):
        if p2<a:
            p2+=int(input("enter value P2:"))
            if p2>=a:
                print("p2 win",a)
                break
    
