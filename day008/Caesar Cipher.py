# 100 Days of Code
# DAY 008
# Created by eduardorabe
# Caesar Cipher

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#  and print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output: "The encoded
#  text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# ðBug alert: What happens if you try to encode the word 'civilization'?ð

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
#  amount and print the decrypted text. e.g. cipher_text = "mjqqt" shift = 5 plain_text = "hello" print output: "The
#  decoded text is hello"

# TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call
#  the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND*
#  decrypt a message.

# TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar().

# TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

# TODO-9: Import and print the logo from art.py when the program starts.

# TODO-10: What if the user enters a shift that is greater than the number of letters in the alphabet?

# TODO-11: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me at 3"
# end_text = "â¢â¢â¢â¢ â¢â¢ â¢â¢ 3"

# TODO-12: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

from art import logo


def caesar(text, shift, direction):
    final_text = ""
    shift = shift % 26
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"The {direction}d text is {final_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    question = input("Do you want to continue using the program? (yes or no)?\n")
    if question == "no":
        should_continue = False
        print("Goodbye")
