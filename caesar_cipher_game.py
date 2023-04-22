# This is an Encyption and Decryption Game.You can add adiitional ASCII arts.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            index_of = alphabet.index(letter)
            new_position = alphabet[(index_of + shift) % 26]  # use modulus operator to ensure shift is within range of 26
            cipher_text += new_position
        else:
            cipher_text += letter
    print(f'Encrypted data for the given text is {cipher_text}')

def decrypt(cipher_text, shift):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            index_of = alphabet.index(letter)
            new_position = alphabet[(index_of - shift) % 26]  # use modulus operator to ensure shift is within range of 26
            plain_text += new_position
        else:
            plain_text += letter
    print(f'Decrypted data for the given text is {plain_text}\n')

def caesar():
    if direction == "encode":
        encrypt(plain_text=text, shift=shift_amount)
    elif direction == "decode":
        decrypt(cipher_text=text, shift=shift_amount)

should_end = False
while not should_end:
    direction = input("Type 'encode' for Encryption, 'decode' for Decryption, and 'quit' to Exit.\n").lower()
    text = input(f"Enter text to {direction}:\n").lower()
    shift_amount = int(input("Enter the shift number:\n")) % 26  # use modulus operator to ensure shift is within range of 26
   
    caesar()
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
