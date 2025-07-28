# Create a function-based utility that splits expenses evenly among people.
        
def split_expenses():
    people = input("Enter names separated by comma: ").split(",")
    total = float(input("Enter total amount spent: "))
    
    share = round(total / len(people))
    
    print("\n Expense Splitter Result:")
    for person in people:
        print(f"{person.strip()} owes ₹{share}")

split_expenses()


# def split_expense():
#     # person1=input("enter your name:")
#     # person2=input("enter your name:")
#     # person3=input("enter your name:")
#     persons=input("enter your names (seperated by comma):").split(",")
#     total=float(input("enter total amount:"))
#     split=round(total/len(persons),2)
#     for i in persons:
#         print(f"{i} have to pay ${split}")
        
# split_expense()