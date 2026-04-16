print("Welcome to the tip calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
number_of_people = int(input("How many people to split the bill?"))

tip_percentage = tip/100
total_bill = bill + (bill * tip_percentage)
cost_per_person = total_bill / number_of_people

print(f"Each person should pay ${cost_per_person:.2f}")
