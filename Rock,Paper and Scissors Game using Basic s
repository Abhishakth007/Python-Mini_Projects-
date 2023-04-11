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
game_images = [rock,paper,scissors]
user_counter = 0
computer_counter = 0
for i in range (0,9):
    user_choice = int(input("Enter 0 for rock, 1 for paper , 2 for scissors\n"))
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(game_images[computer_choice])

    if user_choice>3 or user_choice<0:
        print("Enter a valid number")
    elif user_choice==0 and computer_choice == 0 or user_choice== 1 and computer_choice ==1 or user_choice== 2 and computer_choice ==2:
        print('Ohhh... Its a Draw')
    elif user_choice == 0 and computer_choice== 2 or user_choice== 1 and computer_choice == 0 or user_choice== 2 and computer_choice ==1:
        print("Congrats You Won...!!!")
        user_counter +=1
    elif user_choice == 1 and computer_choice== 2 or user_choice== 2 and computer_choice == 0 or user_choice== 0 and computer_choice ==1:
        print("You Lost..Try Again.")
        computer_counter+=1
    else:
        print("SomeThing Went Wrong :()")

print(f"Final Score of the user is {user_counter}.")
print(f"Final Score of the computer is {computer_counter}.")

if user_counter > computer_counter:
    print("you are the champion ...:)")
elif user_counter < computer_counter :
    print("Computer is the champion ..you lost")
else :
    print("Scores are level")

