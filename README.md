# Python Calculator

A simple, interactive Python console-based calculator designed to perform common arithmetic operations and quick number checks. The program runs in the terminal, prompts the user for input, and continues until the user chooses to exit.

## Features

- Addition, subtraction, multiplication, and division
- Modulus calculation
- Power and floor division
- Square root calculation
- Maximum and minimum of two numbers
- Odd/even number detection
- Repeated calculation loop with input validation

## Requirements

- Python 3.x

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run:

```bash
python Python_calc.py
```

## Available Operations

The program supports the following commands:

- `+` — addition
- `-` — subtraction
- `*` — multiplication
- `/` — division
- `%` — modulus
- `**` — exponentiation
- `//` — floor division
- `sr` — square root
- `max` — maximum of two numbers
- `min` — minimum of two numbers
- `odd` — checks whether a number is odd
- `even` — checks whether a number is even

## Example Usage

```text
===============================
         CALCULATOR
===============================
Enter your choice (% ,+ ,- , * ,/ ,** ,// ,sr(Square Root) ,max (Maximum of Two numbers) ,min (Minimum of Two numbers) ,odd , even: +
Enter the first number: 12
Enter the second number: 8
Addition of 12 + 8 is: 20
Do you want to do another calculation? (yes or no): yes
```

## Behavior

- The calculator keeps running until the user enters `no` when prompted.
- Invalid menu choices display an error message and prompt the user again.
- Division by zero is handled safely with a clear message.
- The program uses basic input validation for successful execution.

## Project Files

- `Python_calc.py` — main calculator logic
- `LICENSE` — repository license

## License

This project is distributed under the repository's license terms. Please review the `LICENSE` file for details.

## Contributing

Contributions, improvements, and bug fixes are welcome. If you'd like to enhance the calculator, consider improving the user interface, adding more mathematical functions, or refining input validation.
