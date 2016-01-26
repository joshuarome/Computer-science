# Task 1: Keyword cipher

Analyse the requirements for this program and design, develop, test and evaluate a program to enter, 
encrypt and decrypt messages.

## 1. Requirements
The Caesar cipher system must:

1. Handle non alphabetical plain/cipher text (including spaces)
2. Handle keyword letter shifts which go out of bounds
3. Handle upper and lowercase values
4. Take keywords of any length

> Note: although the task requires a keyword of any length to be accepted, this is impossible; depending on your system there's a limited about of memory which can be allocated, by using pythons `sys` module and its `maxsize` variable this can be seen. A simple test can be carried out to prove this theory:
```python
>>> import sys
>>> "a"*sys.maxsize
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
MemoryError
```
Thus meaning the requirment has to be changed, rather than accepting a keyword of any length, it must accept any keyword length before the max memory limit.

5. Take, validate and cipher the users input. Example run:

```bash
Do you want to encode or decode? (E, D)
> E

What is your plain/cipher text?
> COMPUTINGISFUN

What is your keyword to be ciphered/deciphered by?
> GCSE

Your ciphered/deciphered text is: JRFUBWBSNLLKBQ

Do you want to start again? (Y, N)
> N
```

## 2. Design
The  keyword cipher has been built assuming that it will be run from a terminal or Pythons IDLE.
The variables and functions have all been documented in `kw_cipher.py` itself. The doc strings address the requirments listed at the top of this document, in case you do not know how python’s doc strings work:

Either look at the source code or import `kw_cipher.py` as a module and print the `__doc__` property of each function (`cipher`, `get_choice` and `main`).

The keyword cipher has been designed with two different approaches: pseudocode and a flow chart.

Pseudocode:
```c
Start keyword cipher;

Request cipher choice;
Request plain/cipher text;
Request keyword;

while(cipher choice is invalid (E or D)) {
  Display error;
  Request cipher choice;
}

if(choice is D) {
  Make keyword letter shift negative to decode;
}

For each character in plain/cipher text and keyword;
if(character is alphabetical) {
  Display character of plain/cipher text + character of keyword;
}

else {
  Displayer character;
}

End;
```

Flowchart:

![Flowchart](http://code2flow.com/ERhACi.png)

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

try:
    from caesar_cipher import get_choice
except ImportError:
    print("Error: 'caesar_cipher.py' must be in the same directory in order to work")
    sys.exit(1)

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
            if not keyw[i].isalpha():
                cipher_text.append(ch)
                continue
            
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
```

> Note: this program requires `caesar_cipher.py` to bw in the same directory otherwise it wont work properly; this is due to the fact that instead of copying and pasting code (which is somewhat inefficiant) it has been reused. If you require the code to not rely on a module I have created a version here: https://bpaste.net/show/aee5c022b3c4

Evaluation:

1. None alphabetical characters are handled on line 50 and 64; each letter is checked to see if they're alphabetical, if they're then thh program progresses onto the next logical step to cipher it. However, if the letter is not alphabetical, then the ciphering process is skipped and it is added to the result unchanged.
2. Letters are kept in the alphabet at line 63; modulus has been used with 26 to keep each letter in the alphabet.
3. Upper/lower case values are handled mainly at line 56; the offset variable keeps the letter into the ASCII values, since capitals and non capital values vary it has made use of a one line if else statement to check if it's upper or not.
4. Keywords of any length are taken at line 106.
