#!/usr/bin/python3

from random import choices
from string import ascii_letters, digits, punctuation
import pyperclip

"""Request for options and make a random generator of length specified by user.
Create default values for generator values.

User may want memorable pass, exclude puncts, digits

easy to say: lower+upper
easytorread: same + num/digits
allchars
length
"""


def password_strength():
    password = input("Enter your password: ")
    # if len(password) < 8 or
    print("Weak")


def generate_password(char_set, length):
    if length in [None, "", " "]:
        length = 12
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


def main():
    print("1. Check Password Strength\n2. Generate Password")
    try:
        usage = int(input("Enter choice: "))
    except ValueError:
        pass

    if usage == 1:
        password_strength()
    elif usage == 2:
        password_gen_helper()


if __name__ == "__main__":
    main()
