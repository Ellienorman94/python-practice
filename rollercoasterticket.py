print("Welcome to the Cruising Coaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print ("You can ride the Cruising Coaster!")
    age = int(input("How are are you?"))
    if age <= 12:
        bill = 5
        print("Child tickets are £5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are £7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You can ride the Cruising Coaster for free!")
    else:
        bill = 12
        print("Adult tickets are £12")

    buy_photo = input("Would you like to buy a photo? Y or N:")
    if buy_photo == "Y":
     bill += 3

     print(f"Your total bill is {bill}")

else:
 print("Sorry you're too small to ride the Cruising Coaster!")
