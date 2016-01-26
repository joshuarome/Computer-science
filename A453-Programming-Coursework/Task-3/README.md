# Task 3: File cipher

Analyse the requirements for this program and design, develop, test and evaluate a program to enter, 
encrypt and decrypt messages.

1. Handle non alphabetical plain/cipher text (including spaces)
2. Handle keyword letter shifts which go out of bounds
3. Handle upper and lowercase values
4. Take keywords of any length
5. Handle invalid file names

> Note: although the task requires a keyword of any length to be accepted, this is impossible; depending on your system there's a limited about of memory which can be allocated, by using pythons `sys` module and its `maxsize` variable this can be seen. A simple test can be carried out to prove this theory:
```python
>>> import sys
>>> "a"*sys.maxsize
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
MemoryError
```
Thus meaning the requirment has to be changed, rather than accepting a keyword of any length, it must accept any keyword length before the max memory limit.

6. Take, validate and cipher the users input. Example run:

```bash
Do you want to encode or decode? (E, D)
> E

What is your file name?
> test.txt

What is your keyword to be ciphered/deciphered by?
> abcde

What is your second keyword to be ciphered/deciphered by?
> fghij

Do you want to start again? (Y, N)
> N
```bash

## 2. Design
The  file cipher has been built assuming that it will be run from a terminal or Pythons IDLE.
The variables and functions have all been documented in `kw_cipher.py` itself. The doc strings address the requirments listed at the top of this document, in case you do not know how python’s doc strings work:

Either look at the source code or import `file_cipher.py` as a module and print the `__doc__` property of each function (`cipher`, `get_choice` and `main`).

The file cipher has been designed with two different approaches: pseudocode and a flow chart.

Pseudocode:
```c
Start keyword cipher;

Request cipher choice;
Request file name;
Request keyword;
Request keyword2;

while(cipher choice is invalid (E or D)) {
  Display error;
  Request cipher choice;
}

if(choice is D) {
  Make keyword letter shift negative to decode;
}

For each character in plain/cipher read file and keyword + keyword2;
if(character is alphabetical) {
  Display character of plain/cipher text + character of keyword + keyword 2;
}

else {
  Displayer character;
}

End;
```

Flowchart:

![Flowchart](http://code2flow.com/sziWOX.png)

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
    from kw_cipher import cipher
    from kw_cipher import get_choice
except ImportError:
    print("Error: 'kw_cipher.py' must be in the same directory in order to work")
    sys.exit(1)

def main() -> int:
    """
    stores all the code that runs the program.
    
    This function calls cipher with the users desired choice, text and keyword
    twice with the second time calling the second keyword. The user then has
    an option to restart or exit. If any input is invalid then the program
    displays and error prompt making the user to input again.
    
    Note: the main code has been inserted into a
    function as it's good practice to make variables local rather than 
    global.
    
    vars:
        - parser: ArgumentParser which parses the arguments

        - args: Namespace which stores the arguments

        - choice: string which stores the users choice to encode or decode

        - file_name: string which stores the name of the ciphering file

        - text: string which stores the text to be ciphered/deciphered

        - keyword1: the keyword to be ciphered by

        - keyword2: the second keyword to be ciphered by
        
    return:
        int
    """
    #if args passed from terminal
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        
        parser.add_argument("-c", "--choice", help="the choice to encode or decode (E, D)", choices = ("E", "e", "D", "d"))
        parser.add_argument("-f", "--file_name", help="the file which contains the text to be ciphered/deciphered")
        parser.add_argument("-k1", "--keyword1", help="the keyword to be ciphered by")
        parser.add_argument("-k2", "--keyword2", help="the secondkeyword to be ciphered by")
        
        args = parser.parse_args()

        try:
            with open(args.file_name, "r") as f:
                text = f.read()
        except FileNotFoundError:
            print("\nInvalid input, file not found")
            sys.exit(1)

        with open(args.file_name, "w") as f:
            f.write(cipher(args.choice, cipher(args.choice, text, args.keyword1), args.keyword2))
    
    else:
        #program loop
        while True:
            choice = get_choice("Do you want to encode or decode?", ("E", "D"))
            
            #file validation loop
            while True:
                file_name = input("\nWhat is your file name?\n> ")
                
                try:
                    with open(file_name, "r") as f:
                        text = f.read()
                    break
                except FileNotFoundError:
                    print("\nInvalid input, file not found")

            keyword1 = input("\nWhat is your keyword to be ciphered/deciphered by?\n> ")
            keyword2 = input("\nWhat is your second keyword to be ciphered/deciphered by?\n> ")

            with open(file_name, "w") as f:
                f.write(cipher(choice, cipher(choice, text, keyword1), keyword2))

            if get_choice("\nDo you want to start again?", ('Y', 'N')) == "N":
                #exit program
                break

            print()

    #clean exit
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

> Note: this program requires `kw_cipher.py` and `caesar_cipher.py" to bw in the same directory otherwise it wont work properly; this is due to the fact that instead of copying and pasting code (which is somewhat inefficiant) it has been reused. If you require the code to not rely on a module I have created a version here: https://bpaste.net/show/e23b52036bfe

Evaluation:
