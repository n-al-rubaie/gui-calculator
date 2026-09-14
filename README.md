# Simple Command-Line Calculator

A beginner-friendly **command-line calculator built with Python**. The application allows users to perform normal arithmetic calculations directly in the terminal.

It also provides a calculation history system that saves every successful calculation with the current date and time.

## Features

* Command-line interface
* Addition
* Subtraction
* Multiplication
* Division
* Remainder using `%`
* Floor division using `//`
* Power operation using `**`
* Calculation history
* Timestamp added to every calculation
* View previous calculations
* Clear calculation history
* Help command
* Exit command
* Invalid input handling
* Invalid number handling
* Division-by-zero protection
* No scientific calculation functions

## Technologies Used

* **Python 3**
* **Datetime Module**
* **File Handling**
* **Conditional Statements**
* **Functions**
* **Exception Handling**
* **Loops**

## Project Structure

```text
Simple-Command-Line-Calculator/
│
├── calculator.py
├── history.txt
└── README.md
```

### File Description

| File            | Description                                |
| --------------- | ------------------------------------------ |
| `calculator.py` | Main Python program                        |
| `history.txt`   | Stores calculation history with timestamps |
| `README.md`     | Project documentation                      |

## Supported Operations

| Operation      | Example   | Output |
| -------------- | --------- | -----: |
| Addition       | `10 + 5`  |   `15` |
| Subtraction    | `10 - 5`  |    `5` |
| Multiplication | `10 * 5`  |   `50` |
| Division       | `10 / 5`  |    `2` |
| Remainder      | `10 % 3`  |    `1` |
| Floor Division | `10 // 3` |    `3` |
| Power          | `2 ** 3`  |    `8` |

## Requirements

* Python 3.x
* No external Python packages are required.

The `datetime` module is included with Python, so it does not need to be installed separately.

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/simple-command-line-calculator.git
```

### 2. Open the Project Folder

```bash
cd simple-command-line-calculator
```

### 3. Run the Program

```bash
python calculator.py
```

## How to Use

Enter a calculation in this format:

```text
number operator number
```

Example:

```text
10 + 20
```

Output:

```text
Result: 30
```

### Available Commands

| Command   | Function                       |
| --------- | ------------------------------ |
| `history` | Displays previous calculations |
| `clear`   | Clears all saved history       |
| `help`    | Displays available commands    |
| `exit`    | Closes the calculator          |

## Example Usage

```text
WELCOME TO THE SIMPLE CALCULATOR
Type 'help' to see all commands.

Enter calculation or command: 10 + 20
Result: 30

Enter calculation or command: 50 / 5
Result: 10

Enter calculation or command: history
[14-09-2026 12:30:45] 50 / 5 = 10
[14-09-2026 12:30:30] 10 + 20 = 30
```

## Calculation History

The program stores calculations in `history.txt`.

Each record contains:

* Date
* Time
* Equation
* Result

Example:

```text
[14-09-2026 12:30:45] 10 + 20 = 30
```

## Error Handling

The calculator handles:

* Invalid input format
* Invalid numbers
* Invalid operators
* Division by zero
* Remainder by zero
* Very large results

## Limitations

* The calculator works through the terminal.
* Calculations must be entered in the format `number operator number`.
* Scientific operations are not included.
* History is stored locally in a text file.
* It supports two-number calculations only.

## Future Improvements

* Add keyboard shortcuts
* Add a graphical user interface
* Add memory functions
* Add CSV export for history
* Add support for multi-step calculations
* Add unit conversion features
* Add calculation history search

## Learning Outcomes

This project helped develop knowledge of:

* Python functions
* `if-elif-else` statements
* `while` loops
* File handling
* Exception handling
* Date and time formatting
* User input handling
* Basic arithmetic operations
* Code organization

## Author

**Divyansh Dubey**


## License

This project is created for educational and learning purposes.
