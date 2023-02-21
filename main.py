#!/usr/bin/python3

from random import choices
from string import ascii_letters, digits, punctuation
import pyperclip


def password_validator(passwd):

    strength = 0

    length = len(passwd)
    # Check length
    if length > 8:
        strength += 1

    if any(char.isdigit() for char in passwd):
        strength += 1

    if any(not char.isalnum() for char in passwd):
        strength += 1

    if any(char.islower() for char in passwd) or any(char.isupper() for char in passwd):
        strength += 1

    return strength


def password_strength(passwd):
    validation = password_validator(passwd)

    indicator = ""
    if validation < 2:
        indicator += "Password is very weak"
    elif validation == 2:
        indicator += "Password is weak"
    elif validation == 3:
        indicator += "Password is strong"
    elif validation == 4:
        indicator += "Password is very strong"

    print(indicator)


def generate_password(char_set, length):
    return "".join(choices(char_set, k=length))


def password_gen_helper():

    length = (input("Enter length of password: "))

    print("1. Easy to say 2. Easy to read 3. All characters")
    password_options = int(input("Select you choice: "))

    if length in [None, ValueError, " ", ""]:
        length = 12
    else:
        length = int(length)

    if password_options == 1:
        char_set = ascii_letters
    elif password_options == 2:
        char_set = ascii_letters + digits
    elif password_options == 3:
        char_set = ascii_letters + digits + punctuation

    generated_password = generate_password(char_set, length)
    pyperclip.copy(generated_password)
    print(generated_password)
    print("Password copied to clipboard")
    password_strength(generated_password)


def main():
    print("1. Check Password Strength\n2. Generate Password")
    try:
        usage = int(input("Enter choice: "))
    except ValueError:
        pass

    if usage == 1:
        password = input("Enter your password: ")
        password_strength(password)
    elif usage == 2:
        password_gen_helper()


if __name__ == "__main__":
    main()
