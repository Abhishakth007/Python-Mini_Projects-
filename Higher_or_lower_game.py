import random
from game_data import data
from art import logo,vs
from replit import clear
score_counter = 0
game_end = False

def data_selection():
          """ Gets data from data.py"""
          return random.choice(data)
        

account1 = data_selection()
account2 = data_selection()
if account1 == account2:
          account2 = random.choice(data)
        
        
def data_representation(account_a):
              account_name = account_a["name"]
              account_profession = account_a['description']
              account_country = account_a["country"]
              return f'{account_name} is {account_profession} from {account_country}.'
        
        
def higher_or_lower(guess ,followers_a,followers_b):
            if followers_a >= followers_b:
              return guess == 'a'
            elif followers_b > followers_a:
              return guess == 'b'
        
while not game_end:
          print(logo)
          print(f'Your current score is {score_counter}.')
          print(f'Compare A : {data_representation(account_a = account1)}')
          print(vs)
          print(print(f'Compare B : {data_representation(account_a = account2)}'))
          guess = input("Type 'A' or 'B'' to make the right choice.")
          account1_followers = account1["follower_count"]
          account2_followers = account2["follower_count"]
          higher_or_lower_checker = higher_or_lower(guess,account1_followers, account2_followers )
           
          clear()

          if higher_or_lower_checker == True:
            score_counter +=1
            print("Yes u are right. ")
            print(f'you current score is {score_counter}')
            account1 = account2
            account2 = data_selection()
          else:
            print("Oh no its incorrect.")
            print(f'your final score is {score_counter}.')
            game_end = True
              
          
            
