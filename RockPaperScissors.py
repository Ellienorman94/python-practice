rock = '''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
  _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = ''' 
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print ("Lets play Rock, Paper, Scissors!")

question = input("rock, paper, scissors?: ")

if question == "rock":
 print(rock)
elif question == "paper":
 print(paper)
elif question == "scissors":
 print(scissors)
else:
 print ("Invalid choice")

import random
decision = ["rock", "paper", "scissors"]
random_index= random.randint(0,2)
if random_index == 0:
 print(rock)
elif random_index == 1:
 print(paper)
else:
    print(scissors)

computer_choice = decision[random_index]

if question == computer_choice:
    print("It's a draw!")
elif question == "rock" and computer_choice == "scissors":
    print("You win!")
elif question == "paper" and computer_choice == "rock":
    print("You win!")
elif question == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("You lose!")










