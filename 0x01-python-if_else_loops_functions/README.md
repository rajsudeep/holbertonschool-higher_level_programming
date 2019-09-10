# Python - Hello, World
## General Concept Guidance:
* [More Control Flow Tools](https://docs.python.org/3.4/tutorial/controlflow.html)
* [Learn to Program (in Python)](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
### [0. Positive anything is better than negative nothing](./0-positive_or_negative.py)
> The output of the program should be:
> * The number, followed by
>   * if the number is greater than 0: is positive
>   * if the number is 0: is zero
>   * if the number is less than 0: is negative
### [1. The last digit](./1-last_digit.py)
> The output of the program should be:
> * The string Last digit of, followed by
> * the number, followed by
> * the string is, followed by the last digit of number, followed by
>   * if the last digit is greater than 5: the string and is greater than 5
>   * if the last digit is 0: the string and is 0
>   * if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
### [2. I play what I call the alphabet game](./2-print_alphabet.py)
> Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line
### [3. When I was having that alphabet soup, I never thought that it would pay off](./3-print_alphabt.py)
> Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line
> * Print all the letters except q and e
### [4. Hexadecimal printing](./4-print_hexa.py)
> Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal
### [5. 00...99](./5-print_comb2.py)
> Write a program that prints numbers from 0 to 99
### [6. Inventing is a combination of brains and materials](./6-print_comb3.py)
> Write a program that prints all possible different combinations of two digits
### [7. islower](./7-islower.py)
> Write a function that checks for lowercase character
### [8. To uppercase](./8-uppercase.py)
> Write a function that prints a string in uppercase followed by a new line
### [9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important](./9-print_last_digit.py)
> Write a function that prints the last digit of a number
### [10. a + b](./10-add.py)
> Write a function that adds two integers and returns the result
### [11. a ^ b](./11-pow.py)
> Write a function that computes a to the power of b and return the value
### [12. Fizz Buzz](./12-fizzbuzz.py)
> Write a function that prints the numbers from 1 to 100 separated by a space
> * For multiples of three print Fizz instead of the number and for multiples of five print Buzz
> * For numbers which are multiples of both three and five print FizzBuzz
### [13. Insert in sorted linked list](./13-insert_number.c)
> Write a function in C that inserts a number into a sorted singly linked list
### [100. Smile in the mirror](./100-print_tebahpla.py)
> Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase
### [101. Remove at position](./101-remove_char_at.py)
> Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”)
### [102. ByteCode](./102-magic_calculation.py)
> Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
```   3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```