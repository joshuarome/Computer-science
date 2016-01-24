# Task 1: Caesar cipher

Analyse the requirements for this program and design, develop, test and evaluate a program to enter, 
encrypt and decrypt messages.

## 1. Requirements
The Caesar cipher system must:

1. Handle non alphabetical plain/cipher text
2. Handle non integer shift values
3. Handle shifts which go out of bounds
4. Handle upper and lowercase values
5. Take, validate and cipher the users input. Example run:

```bash
Do you want to encode or decode? (E, D)
> E

What is your plain/cipher text?
> COMPUTING IS FUN

What is your shift?
> 5

Your encoded/decoded text is: HTRUZYNSL NX KZS

Do you want to start again? (Y, N)
> N
```
 
## 2. Design
The Caesar cipher has been built assuming that it will be run from a terminal or Pythons IDLE.
The variables and functions have all been documented in `caesar_cipher.py` itself. The doc strings address the requirments listed at the top of this document, in case you do not know how python’s doc strings work:

Either look at the source code or import `caesar_cipher.py` as a module and print the `__doc__` property of each function (`cipher`, `get_choice` and `main`).

The Caesar cipher has been designed with two different approaches: pseudocode and a flow chart.

Pseudocode:
```c
Start caesar cipher;

Request cipher choice;
Request plain/cipher text;
Request shift;

while(cipher choice is invalid (E or D)) {
  Display error;
  Request cipher choice;
}

if(choice is D) {
  Make shift negative to decode;
}

For each character in plain/cipher text;
if(character is alphabetical) {
  Display character + shift;
}
 
else {
  Displayer character;
}

End;
```
Flowchart:

![Flowchart](http://code2flow.com/uP4lVX.png)

## 3. Development
Development choices:

When developing this program, Python 3+ was chosen for multiple reasons: When compared to a language like Java, Python programs are generally expected to run slower than Java programs they also take much less time to develop. Python programs are typically 3-5 times shorter than equivalent Java programs. This difference can be attributed to Python's built-in high-level data types and its dynamic typing (source(s) and more information can be found at: https://www.python.org/doc/essays/comparisons/)

I shan't state all the functions/methods/statements/loops etc. used as most of them are self-explanatory and this is not a python tutorial, but the functions `ord` (https://docs.python.org/3/library/functions.html#ord) and `chr` (https://docs.python.org/3/library/functions.html#chr) to cipher/decipher the characters, and the loops `for` and `while` were used to iterate and validate.

The inbuilt module `sys` has been used to exit the program with a clean exit status (0) if the program executed without problems, if problems were encountered then the program will exit with a non 0 status - this has been implemented to indicate if the program has ran correctly in the terminal.

Another inbuilt module `argparse` has been used to easily create terminal arguments (as specified in the requirements)

Test plan:

As previously stated the testing of the programs final product must be documented so it has been documented with a validation table.

Validated inputs:
- the users choice to encode or decode:

Input  | Purpose | Result
------------- | ------------- | -------------
Other values than E or D  | Check how the system handles other values than E or D | Output rejected displaying an error message asking to try again
E and D  | Check how the system handles E and D | Output accepted and the program continues to the next logical step

Program test run:
```bash
Do you want to encode or decode? (E, D)
> !

Invalid input, must be in (E, D)

Do you want to encode or decode? (E, D)
> 1.2

Invalid input, must be in (E, D)

Do you want to encode or decode? (E, D)
> a

Invalid input, must be in (E, D)

Do you want to encode or decode? (E, D)
> E
```

- the users cipher shift:

Input  | Purpose | Result
------------- | ------------- | -------------
Non integer values  | Check how the system handles non integer values | Output rejected displaying an error message asking to try again
123456789  | Check how the system handles integer values | Output accepted and the program continues to the next logical step

Program test run:
```bash
What is your shift?
> !

Invalid input, must be an integer

What is your shift?
> 1.2

Invalid input, must be an integer

What is your shift?
> a

Invalid input, must be an integer

What is your shift?
> 1

Your encoded/decoded text is: ...
```

- the users choice to restart or exit:

Input  | Purpose | Result
------------- | ------------- | -------------
Other values than Y or N  | Check how the system handles other values than Y or N | Output rejected displaying an error message asking to try again
Y and N  | Check how the system handles Y and N | Output accepted and the program continues to the next logical step

Program test run:
```bash
Do you want to start again? (Y, N)
> !

Invalid input, must be in (Y, N)


Do you want to start again? (Y, N)
> 1.2

Invalid input, must be in (Y, N)


Do you want to start again? (Y, N)
> a

Invalid input, must be in (Y, N)


Do you want to start again? (Y, N)
> Y

Do you want to encode or decode? (E, D)
> 
```

The terminal arguments are automatically checked and validated by the `argparse` module itself, so creating a test plan for it was not necessary

Development stages:

When developing this program, many development choices were made:
- cipher_text was changed to type list from list to prevent quadratic runtime:
```python
cipher_text = ""
...
cipher_text += letter
...
```
- the main code was placed in a function to avoid the dangers of global variables
- the cipher function used while loops to keep each letter within the alphabet so it was replaced with clever math using modulus to prevent slow running times:
```python
while letter > ord("Z"):
    letter -= 26
    
while letter < ord("A"):
    letter += 26
```
- recursive functions were used for validation which can cause the program to fail so it was replaced with a while loop:
```python
def get_choice(...):
    ...
    get_choice()
    ...
```

Final product:
```python
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
```

Evaluation:

1. None alphabetical characters are handled on line 46 and 49; each letter is checked to see if they're alphabetical, if they're then thh program progresses onto the next logical step to cipher it. However, if the letter is not alphabetical, then the ciphering process is skipped and it is added to the result unchanged.
2. Non integer shift values are handled at 128 to 134; the program attempts to convert the users input to an int, if it fails then it displays an error (as it must not be an integer value).
3. Letters are kept in the alphabet at line 48; modulus has been used with 26 to keep each letter in the alphabet.
4. Upper/lower case values are handled mainly at line 44; the offset variable keeps the letter into the ASCII values, since capitals and non capital values vary it has made use of a one line if else statement to check if it's upper or not.
5. Input is took, validated and processed in the multiple functions cipher, get_choice and main; the cipher function ciphers certain text by a choice and shift, the get_choice function gets the users input and validates it only accepting certain values and finally the main function is where the main code takes place, it's where the functions are called and input is taken (detailed information of these functions can be found in the functions doc strings).
