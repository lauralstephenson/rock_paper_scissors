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

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]
#First the user is asked to choose rock, paper or scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#Make sure the user puts in a valid input
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
#Now the user choice is printed
print("You chose:")
print(game_images[user_choice])
#Then the computer randomly chooses rock, paper or scissors
computer_choice = random.randint(0, 2)
print("The computer chose:")
print(game_images[computer_choice])
#Then the results are printed
#Rock wins against scissors.
#Scissors wins against paper.
#Paper wins against rock.
#The same choice for both sides is a draw.
if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice > user_choice:
  print("You lose!")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw! Try again!")