#!/usr/bin/python3

import sys
import argparse

def cipher(choice: str, text: str, shift: int) -> str:
    """
    ciphers text by shift and returns the ciphered value
    
    This function encodes or decodes text depending on choice, text is then
    iterated through checking if each character is upper or lower case to
    cipher correctly. Modulos has been used to keep each character in the
    alphabet. The character is only ciphered if the character is alphabetical,
    non alphabetical values will be left the same. The value is then appended
    to cipher_text and is returned as a string
    
    args:
        - choice: string which stores the users choice to encode or decode

        - text: string which stores the text to be ciphered/deciphered

        - shift: int which stores the shift to be ciphered by
        
    vars:
        - cipher_text: list which will hold the characters of the ciphered text.
            The type list has been chosen over string as strings are immutable
            thus meaning repetitive string concatenation may result in quadratic
            runtime
        
        - offset: int which stores the anchor point for upper/lower case letters
        
        - letter: string which stores the ciphered letter
    
    return:
        string which stores the ciphered text
    """
    cipher_text = []

    if choice.upper() == "D":
        shift = -shift

    for ch in text:
        #anchor point for upper/lower case letters
        offset = ord("A") if ch.isupper() else ord("a")
        
        if ch.isalpha():
            #keep letter in alphabet (26 letters in alphabet)
            letter = chr((ord(ch) - offset + shift) % 26 + offset)
        else:
            letter = ch
            
        cipher_text.append(letter)
        
    return "".join(cipher_text)

def get_choice(prompt: str, valid: tuple) -> str:
    """
    returns a validated choice
    
    This function prompts the user with prompt with the valid choices and only
    breaks if the input is in valid.
    
    args:
        - prompt: string which stores the prompt message
        
        - valid: iterable which stores the valid input values
        
    vars:
        - choice: string which stores the users choice
    
    return:
        string which stores the validated choice
    """
    while True:
        choice = input("{} ({})\n> ".format(prompt, ", ".join(valid))).upper()

        if choice not in valid:
            print("\nInvalid input, must be in ({})\n".format(", ".join(valid)))
            continue
        
        return choice

def main() -> int :
    """
    stores all the code that runs the program.
    
    This function calls cipher with the users desired choice, text and shift.
    If the shift is an integer then the function is called correctly and the
    ciphered value is displayed, otherwise an error prompt is displayed
    making the user try again. The user then has an option to restart or exit.
    
    Note: the main code has been inserted into a
    function as it's good practice to make your variables local rather than 
    global.
    
    vars:
        - parser: ArgumentParser which parses the arguments

        - args: Namespace which stores the arguments
    
        - choice: string which stores the users choice to encode or decode

        - text: string which stores the text to be ciphered/deciphered

        - shift: int which stores the shift to be ciphered by

    return:
        None
    """
    #if args passed from terminal
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-c", "--choice", help="the choice to encode or decode (E, D)", choices = ("E", "e", "D", "d"))
        parser.add_argument("-t", "--text", help="the text to be ciphered/deciphered")
        parser.add_argument("-s", "--shift", help="the shift to be ciphered by", type=int)
        
        args = parser.parse_args()
        print(cipher(args.choice, args.text, args.shift))
    
    else:
        #program loop
        while True:
            choice = get_choice("Do you want to encode or decode?", ("E", "D"))
            text = input("\nWhat is your plain/cipher text?\n> ")
            
            #shift validation loop
            while True:
                try:
                    shift = int(input("\nWhat is your shift?\n> "))
                    break
                #shift not an int
                except ValueError:
                    print("\nInvalid input, must be an integer\n")

            print("\nYour encoded/decoded text is:", cipher(choice, text, shift))

            if get_choice("\nDo you want to start again?", ('Y', 'N')) == "N":
                #exit program
                break

            print()

    #clean exit
    return 0
            
#if the file is being ran
if __name__ == "__main__":
    sys.exit(main())