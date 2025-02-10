import random
import string
import sys

def generate_password(minimun_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special_chars

    password = ""
    
    meets_criteria = False
    has_number = False
    has_special_chars = False

    while not meets_criteria or len(password) < minimun_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special_chars = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special_chars

    return password

while True:
    minimum_length = input("enter the minimum length(or type 'exit' to quit):")
    if minimum_length.lower() == 'exit':
        print("thank you for stopping by! Exiting the program...")
        sys.exit()
    try:
        minimum_length = int(minimum_length)
        if minimum_length>0:
            break #Exit the loop if valid input is received
        else:
            print("minimun length must be greater than 0.")
    except ValueError:
        print("invalid input. please enter a number for minimum length or correct your sprlling of 'exit'.")

has_number = input("do you want to have numbers? (y/n):").lower() == "y"
has_special_chars = input("Do you want to have special character? (y/n): ").lower() == "y"

#call the function with user-provided values
password = generate_password(minimum_length, has_number, has_special_chars)
print("the generated password is:", password)