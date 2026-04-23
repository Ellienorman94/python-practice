print ("Welcome to Python Pizza Deliveries")
size = input("What size pizza would you like? S, M or L:")
bill = 0
if size == "S":
    bill= 15
    print ("Small pizza's are £15")

elif size == "M":
        bill = 20
        print("Medium pizza's are £20")
elif size == "L":
    bill= 25
    print("Large pizza's are £25")

pepperoni = input("Would you like pepperoni? Y or N:")
if pepperoni == "Y":
   bill += 2
   print("Pepperoni is £2")

extra_cheese = input("Would you like extra_cheese? Y or N:")
if extra_cheese == "Y":
    bill += 1


print (f"Your final bill is £{bill:.2f}")


