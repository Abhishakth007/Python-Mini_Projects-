import random
print("Hello Budyy... The Empty Blanks contains a name of a name of a Fruit. \n")
print("Try To Guess The Fruit Name Or You Will Lose...watch out for the life_counter")
list_of_words = ["orange","apple","banana","jackfruit","grapes","peach","mango","guava"]
word_to_be_guessed = random.choice(list_of_words)
length_of_word_to_be_guessed = len(word_to_be_guessed)
blanks = []
for i in range(len(word_to_be_guessed)):
  blanks += "_"
 
print(' '.join(blanks))
life_counter = 7
game_over = False
while game_over == False:
    guess = input("\nEnter Your Guess: ").lower()
    for index in range(len(word_to_be_guessed)):
      letter = word_to_be_guessed[index]
      if letter == guess:
        blanks[index] = letter
        print(' '.join(blanks))
      
    if guess not in word_to_be_guessed:
        life_counter -=1
        print("No.of lifes Remaining : ",life_counter)
    if life_counter == 6:
      print(''' +---+
  |   |
      |
      |
      |
      |
=========
                                      ''')
    if life_counter == 5:
      print(''' +---+
  |   |
  O   |
      |
      |
      |
=========       
                                     ''')
    if life_counter == 4:
      print('''  +---+
  |   |
  O   |
  |   |
      |
      |
=========                         
                                    ''')
    if life_counter == 3:
      print('''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
                                         ''')
    if life_counter == 2:
      print('''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
                                      ''')
    if life_counter == 1:
      print('''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
                                      ''')
    if life_counter == 0:
      print(''' +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
                                    ''')
    if "_" not in blanks:
              game_over = True
              print("Game Over..You Won")
   
    if life_counter == 0:
            game_over = True
            print("Game over ..You Lost")    
    
  



      
      
    
