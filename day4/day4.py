# 100 Days of Code
# DAY 4
# Created by eduardorabe
# Rock, Paper and Scissors

import random

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
choices = [rock, paper, scissors]

print("Welcome to Rock, Paper and Scissors game.")
user_choice = int(input("0 for Rock\n1 for Paper\n2 for Scissors\nUser chose: "))
if user_choice <= 2 and user_choice >= 1:
    print(choices[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice} " + choices[computer_choice])

if user_choice < 0 or user_choice >= 3:
    print("Invalid number, you lose!")
elif user_choice == computer_choice:
    print("Draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice < computer_choice:
    print("You lose")
else:
    print("You Win!")
