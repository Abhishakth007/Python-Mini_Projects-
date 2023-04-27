import random

def score_calculator(updated_deck):
      initial_score = 0
      num_of_aces = 0
      for elements in updated_deck:
         if elements == 11:
            num_of_aces += 1
         initial_score += elements
      while initial_score > 21 and  num_of_aces > 0 :
          initial_score -= 10
          num_of_aces -= 1       
      return initial_score

game_end = False

while not game_end:
    want_to_play = input("Type 'y' to play Blackjack game if not type 'n' :\n ")
    if want_to_play =='y':
        deck  = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        computer_deck = []
        computer_card1 = random.choice(deck)
        computer_card2 = random.choice(deck)
        computer_deck = [computer_card1,computer_card2]
        user_deck = []
        card1 = random.choice(deck)
        card2 = random.choice(deck)
        user_deck = [card1,card2]
        current_score = score_calculator(updated_deck = user_deck)
        print(f'Initial user_deck is {user_deck}')
        print(f'Your current score is {current_score}.\n')
        print(f'computer first card is [{computer_deck[0]}]\n')
        if current_score == 21:
          print("Blackjack ... You won.")
          game_end  = True
          break
        

        stand = False
        while not stand and current_score <= 21:
          pick_up = input("types 'y' if you want to take another card if no then type 'n' : " )
          if pick_up == 'y':
              user_deck.append(random.choice(deck))
              current_score = score_calculator(user_deck)
              print(user_deck)
              print(current_score)
              if current_score > 21:
                print("Bust..You lost :(")
                game_end = True
              elif current_score == 21:
                print("BlackJack ..You won!")
                game_end = True
                break
          else:
                stand = True
                print(f'user_score = {current_score}.')
                computer_score = score_calculator(computer_deck)
                print(f'computer_deck = {computer_deck}')
                print(f'computer_score = {computer_score}.')
                if computer_score > current_score:
                     print("Computer won ..")
                     game_end = True
                elif computer_score == 21:
                     print("Ohh Computer won..")
                     game_end = True
                elif computer_score == current_score :
                     print("its a draw.")
                     game_end = True
                     
                while computer_score < 21 and computer_score < current_score:
                  computer_deck.append(random.choice(deck))
                  computer_score = score_calculator(computer_deck)
                  print(computer_deck)
                  print(computer_score)
                  if computer_score > 21:
                    print("Hurray You win ...")
                    game_end = True
                  elif computer_score == current_score:
                    print("Its a draw.")
                    game_end = True
                  elif computer_score == 21:
                    print("Oh no..Computer won")
                    game_end = True
                  elif computer_score > current_score:
                    print("Computer wins..")
                    game_end = True
                    break
                    
                
    else:
      print("Bye")
      game_end = True
