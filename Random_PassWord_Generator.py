import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
total_letters = int(input("Enter how many letters in your password.\n"))
total_symbols = int(input("Enter how many symbols in your password.\n"))
total_numbers = int(input("Enter how many numbers in your password.\n"))
for i in range (0,total_letters):
    letter = random.choice(letters)
    password.append(letter)
for j in range(0,total_symbols):
    symbol= random.choice(symbols)
    password.append(symbol)
for k in range (0,total_numbers):
    number = random.choice(numbers)
    password.append(number)

print(password)
random.shuffle(password)   #random.shuffle method is used to shuffle elements inside a list randomly
print(password)
print(''.join(password))  # join method combines any iterables into a string
