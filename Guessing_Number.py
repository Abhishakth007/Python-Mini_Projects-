import random
print("welcome to the number guessing game..\n")
print("I am thinking of a number between 1 and 100..\n")
secret_number = random.randint(1,101)
level = input("Type 'hard' for hard mode or type 'easy' for easy mode.\n").lower()
def hint(secret,user_choice):
    if secret == user_choice:
      print("Yes u won \n")
      return True
    else:
      difference = secret - user_choice
      if difference > 0:
        print("too low \n")
        return False
      elif difference <0:
        print("too high \n")
        return False

if level == "hard":
  number_of_attempts = 5
  print("You have 5 chances to guess the secret number\n")
  while number_of_attempts >=0:
    if number_of_attempts == 0 :
      print(f'The secret number is {secret_number}.')
      break
    user_guess = int(input(f'Guess the secret number : '))
    if hint(secret = secret_number , user_choice = user_guess):
      break 
    number_of_attempts -=1
    print(f'you have {number_of_attempts} attempts left\n')
elif level == 'easy':
    number_of_attempts = 10
    print("You have 10 chances to guess the secret number\n")
    while number_of_attempts >=0:
      if number_of_attempts == 0 :
         print(f'The secret number is {secret_number}.')
         break
      user_guess = int(input(f'Guess the secret number : '))
      if hint(secret = secret_number , user_choice = user_guess):
        break 
      number_of_attempts -=1
      print(f'you have {number_of_attempts} attempts left\n')
    

  
