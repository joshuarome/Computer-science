#!/usr/bin/python3

import sys
import argparse

from caesar_cipher import get_choice

def cipher(choice: str, text: str, keyw: str) -> str:
    """
    ciphers text by a keyword and returns the ciphered value
    
    This function encodes or decodes text depending on choice, firstly the
    keyword is stretched to the text length, text is then iterated through
    checking if each character is upper or lower case to cipher correctly.
    Modulos has been used to keep each character in the alphabet. The
    character is only ciphered by the numeric value of the equivalent
    keyword letter if the character is alphabetical, non alphabetical
    values will be left the same. The value is then appended to cipher_text
    and is returned as a string
    
    args:
        - choice: string which stores the users choice to encode or decode

        - text: string which stores the text to be ciphered/deciphered

        - keyw: string which stores the keyword to be ciphered by
        
    vars:
        - cipher_text: list which will hold the characters of the ciphered text.
            The type list has been chosen over string as strings are immutable
            thus meaning repetitive string concatenation may result in quadratic
            runtime
        
        - offset: int which stores the anchor point for upper/lower case letters
        
        - shift: int which stores the shift to be ciphered by
    
    return:
        string which stores the ciphered text
    """
    #stretch keyword to text length
    keyw = (keyw * (len(text) // len(keyw) + 1))[:len(text)]
    cipher_text = []
    
    for i, ch in enumerate(text):
        if ch.isalpha():
            #anchor point for upper/lower case letters
            offset = ord("A") if keyw[i].isupper() else ord("a")
            shift = ord(keyw[i]) - offset + 1
            
            if choice == "D":
                shift = -shift

            #keep letter in alphabet (26 letters in alphabet)
            cipher_text.append(chr((ord(ch) - offset + shift) % 26 + offset))
        else:
            cipher_text.append(ch)
        
    return "".join(cipher_text)

def main() -> int :
    """
    stores all the code that runs the program.
    
    This function calls cipher with the users desired choice, text and keyword.
    The user then has an option to restart or exit. If any input is invalid
    then the program displays and error prompt making the user to input again.
    
    Note: the main code has been inserted into a
    function as it's good practice to make variables local rather than 
    global.
    
    vars:
        - parser: ArgumentParser which parses the arguments

        - args: Namespace which stores the arguments
        
    return:
        int
    """
    #if args passed from terminal
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-c", "--choice", help="the choice to encode or decode (E, D)", choices = ("E", "e", "D", "d"))
        parser.add_argument("-t", "--text", help="the text to be ciphered/deciphered")
        parser.add_argument("-k", "--keyword", help="the keyword to be ciphered by")
        
        args = parser.parse_args()
        print(cipher(args.choice, args.text, args.keyword))
    
    else:
        #program loop
        while True:
            print("\nYour ciphered/deciphered text is:", cipher(
                get_choice("Do you want to encode or decode?", ("E", "D")),
                input("\nWhat is your plain/cipher text?\n> "),
                input("\nWhat is your keyword to be ciphered/deciphered by?\n> ")
                )
            )

            if get_choice("\nDo you want to start again?", ('Y', 'N')) == "N":
                #exit program
                break

            print()

    #clean exit
    return 0
    
if __name__ == "__main__":
    sys.exit(main())
