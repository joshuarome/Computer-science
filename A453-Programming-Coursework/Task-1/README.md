# Task 1: Caesar cipher

Analyse the detailed requirements for each situation and, using suitable 
algorithms, design a solution to be coded in a suitable high-level programming language. Show the 
iterative development of the individual solutions with suitable testing throughout the process. Test 
the final products and evaluate your solutions against the detailed requirements you identified in the 
analysis.

## 1. Requirements
The Caesar cipher system must

- Allow the use of terminal arguments, for example:
  ```bash
caesar_cipher.py --choice "E" --text "Hello" --shift 1 => "Ifmmp"
```
> Note: `=>` indicates the resulting output

- Short hand arguments must also be allowed, for example:
  ```batch
caesar_cipher.py -c "E" -t "Hello" -s 1 => "Ifmmp"
```

- If no terminal arguments have been passed, then the system must take and store the user’s choice, plain/cipher text and shift

- The users input (whether it be from the terminal arguments or not) must be processed (ciphered according to their choice, text and shift). Example run:
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

- The processed input must then be outputted giving the option to restart

- Handle possible errors such as:
 - Non alphabetical plain/cipher text
 - Non integer shift values
 - Shifts which go out of bounds
 - Upper and lowercase values
 - And any other possible errors
 
## 2. Design
The Caesar cipher has been built assuming that it will be run from a terminal or Pythons IDLE.
The variables and functions have all been documented in `caesar_cipher.py` itself, in case you do not know how python’s doc strings work:

Either look at the source code or import `caesar_cipher.py` as a module and print the `__doc__` property of each function (`cipher`, `get_choice` and `main`).

The Caesar cipher has been designed with two different approaches: C style pseudocode (https://en.wikipedia.org/wiki/Pseudocode#Syntax) and a flow chart.

Pseudocode:
```c
void function caesar_cipher {
    print "do you want to encode (e) or decode (d): ";
    set choice to input;

    If choice is not E and D
        print "invalid input";

    print "input the text: ";
    set text to input;

    print "input the shift: ";
    set shift to input;

    If shift is not int
        print "invalid input";

    print "your encoded/decoded test is: ";

    Foreach(character in text)
    {
        If character is alphabetical
            If choice is 'e'
                print character + shift;
            Else
                print character - shift;
        Else
            print character;
    }

}
```
Flowchart:
[INSERT FLOWCHART HERE]

## 3. Development
Development choices:

When developing this program, Python 3+ was chosen for multiple reasons: When compared to a language like Java, Python programs are generally expected to run slower than Java programs they also take much less time to develop. Python programs are typically 3-5 times shorter than equivalent Java programs. This difference can be attributed to Python's built-in high-level data types and its dynamic typing (source(s) and more information can be found at: https://www.python.org/doc/essays/comparisons/)

I shan't state all the functions/methods/statements/loops etc. used as most of them are self-explanatory and this is not a python tutorial, but `ord` (https://docs.python.org/3/library/functions.html#ord) and `chr` (https://docs.python.org/3/library/functions.html#chr) to cipher/decipher the characters.

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
[INSERT DEVELOPMENT STAGES HERE]
