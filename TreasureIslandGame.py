print ("Welcome to Treasure Island!")
print ("Your mission is to find the treasure before the Pirate finds you!")

direction = input("You're at a cross road. Which way do you want to go? left or right?")

if direction == "left":
    swim_wait = input("Would you like to swim or wait?")

    if swim_wait == "wait":
        door_choice = input("Which door would you like to choose? red, blue or yellow?")

        if door_choice == "yellow":
            print ("Congratulations! You won the treasure!")
        elif door_choice == "red" or door_choice == "blue":
         print ("The pirate has caught you! GAME OVER")

    elif swim_wait == "swim":
        print(" The pirate has caught you! GAME OVER")

elif direction == "right":
    print("The pirate has caught you! GAME OVER.")

else:
    print ("Invalid entry. Please try again.")

