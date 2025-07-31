num=1234
i=3
while i>=1:
    n=int(input("enter pin:"))
    if n==num:
        print("log in successful")
        break
    else:
        print(f" Entered wrog Pin ...{i-1}attempts left")
    i-=1