# Simple GUI Calculator

A beginner-friendly graphical calculator built with Python and Tkinter. It uses only Python's standard library, so no additional packages are needed.

## Features

* Number buttons from 0 to 9, decimal point, and sign toggle
* Addition, subtraction, multiplication, and division
* Remainder, floor division, and power operations
* Calculation and result display
* Resizable window with controls that expand to fit
* Clear button
* Custom accent color selection for operation and equals buttons
* Graceful error display, including division-by-zero protection
* Timestamped calculation history, with options to view and clear it

## Requirements

* Python 3.x
* Tkinter (included with most Python installations)

## How to Run

Open a terminal in the project folder and run:

```bash
python Calculator_with_History.py
```

On some systems, use `python3` instead of `python`.

## Using the Calculator

Click number buttons to enter a value, click an operation, enter the next value, and click `=` to calculate. Drag the window edges to resize the calculator; its display and buttons expand with the window. Click `C` to clear the current calculation. Use `Color` to choose an accent color for the operation and equals buttons, and `History` to view or clear saved calculations.

Successful calculations are saved to `history.txt` in the current working directory with a date and time.

## Project Files

| File | Description |
| --- | --- |
| `Calculator_with_History.py` | Calculator logic and Tkinter user interface |
| `history.txt` | Timestamped calculation history |
| `README.md` | Project documentation |

## License

This project is created for educational and learning purposes.
