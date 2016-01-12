# Task 2: Keyword cipher

## 1. Requirements
The keyword cipher system must

- Allow the use of terminal arguments, for example:
  ```bash
kw_cipher.py --choice "E" --text "COMPUTINGISFUN" --keyword "GCSE" => "JRFUBWBSNLLKBQ"
```
> Note: `=>` indicates the resulting output

- Short hand arguments must also be allowed, for example:
  ```batch
kw_cipher.py -c "E" -t "COMPUTINGISFUN" -kw "GCSE" => "JRFUBWBSNLLKBQ"
```

- If no terminal arguments have been passed, then the system must take and store the user’s choice, plain/cipher text and keyword

- The users input (whether it be from the terminal arguments or not) must be processed (ciphered according to their choice, text and keyword). Example run:
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

- The processed input must then be outputted giving the option to restart

- Handle possible errors such as:
 - Non alphabetical plain/cipher text
 - Non integer shift values
 - Keyword shifts which go out of bounds
 - Upper and lowercase values
 - And any other possible errors
 
## 2. Design
The keyword cipher has been built assuming that it will be run from a terminal or Pythons IDLE.
The variables and functions have all been documented in `kw_cipher.py` itself, in case you do not know how python’s doc strings work:

Either look at the source code or import `kw_cipher.py` as a module and print the `__doc__` property of each function (`cipher`, `get_choice` and `main`).

The keyword cipher has been designed with two different approaches: C style pseudocode (https://en.wikipedia.org/wiki/Pseudocode#Syntax) and a flow chart.

Pseudocode:

[INSERT PSEUDOCODE HERE]

Flowchart:

[INSERT FLOWCHART HERE]

## 3. Development
Development choices:

When developing this program, Python 3+ was chosen for multiple reasons: When compared to a language like Java, Python programs are generally expected to run slower than Java programs they also take much less time to develop. Python programs are typically 3-5 times shorter than equivalent Java programs. This difference can be attributed to Python's built-in high-level data types and its dynamic typing (source(s) and more information can be found at: https://www.python.org/doc/essays/comparisons/)

I shan't state all the functions/methods/statements/loops etc. used as most of them are self-explanatory and this is not a python tutorial, but `ord` (https://docs.python.org/3/library/functions.html#ord) and `chr` (https://docs.python.org/3/library/functions.html#chr) to cipher/decipher the characters, the for loop has been used to iterate through text and while loops to validate and loop tasks.

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
[INSERT DEVELOPMENT STAGES HERE]

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
