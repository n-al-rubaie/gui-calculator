from datetime import datetime
import tkinter as tk
from tkinter import colorchooser, messagebox


HISTORY_FILE = "history.txt"


def format_result(result):
    if isinstance(result, float) and result.is_integer():
        return int(result)

    return result


def calculate(first_number, operator, second_number):
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = first_number / second_number
    elif operator == "%":
        if second_number == 0:
            raise ZeroDivisionError("Cannot use zero as the divisor.")
        result = first_number % second_number
    elif operator == "//":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = first_number // second_number
    elif operator == "**":
        result = first_number ** second_number
    else:
        raise ValueError("Invalid operator.")

    if isinstance(result, complex):
        raise ValueError("This calculator supports real-number results only.")

    result = format_result(result)
    if isinstance(result, float) and (result == float("inf") or result == float("-inf")):
        raise OverflowError("The result is too large.")
    return result


def save_to_history(equation, result):
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as history_file:
        history_file.write(f"[{current_time}] {equation} = {result}\n")


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(True, True)
        self.root.minsize(360, 480)
        self.root.configure(padx=12, pady=12, bg="#f2f4f7")

        self.display_value = tk.StringVar(value="0")
        self.equation_text = tk.StringVar(value="")
        self.first_number = None
        self.pending_operator = None
        self.waiting_for_number = False
        self.result_was_shown = False
        self.accent_color = "#84caff"
        self.accent_buttons = []

        self.build_interface()

    def build_interface(self):
        for column in range(4):
            self.root.grid_columnconfigure(column, weight=1, uniform="calculator")
        for row in range(7):
            self.root.grid_rowconfigure(row, weight=1)

        display = tk.Frame(self.root, bg="#f2f4f7")
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 10))

        tk.Label(
            display,
            textvariable=self.equation_text,
            anchor="e",
            font=("Segoe UI", 12),
            fg="#667085",
            bg="#f2f4f7",
            height=1,
        ).pack(fill="x")
        tk.Label(
            display,
            textvariable=self.display_value,
            anchor="e",
            font=("Segoe UI", 28, "bold"),
            fg="#101828",
            bg="#ffffff",
            padx=12,
            pady=12,
        ).pack(fill="both", expand=True)

        self.make_button("History", self.show_history, 1, 0, 1, "#e4e7ec")
        self.make_button("Color", self.choose_color, 1, 1, 1, "#e4e7ec")
        self.make_button("C", self.clear, 1, 2, 2, "#fecdca")

        buttons = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("÷", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("×", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("±", 5, 0), ("0", 5, 1), (".", 5, 2), ("+", 5, 3),
            ("%", 6, 0), ("//", 6, 1), ("xʸ", 6, 2), ("=", 6, 3),
        ]
        for label, row, column in buttons:
            if label.isdigit() or label in (".", "±"):
                command = lambda value=label: self.enter_value(value)
                color = "#ffffff"
            elif label == "=":
                command = self.equals
                color = "#84caff"
            else:
                command = lambda value=label: self.choose_operator(value)
                color = "#e4e7ec"
            button = self.make_button(label, command, row, column, 1, color)
            if label in ("÷", "×", "-", "+", "%", "//", "xʸ", "="):
                self.accent_buttons.append(button)

    def make_button(self, text, command, row, column, columnspan, color):
        button = tk.Button(
            self.root,
            text=text,
            command=command,
            font=("Segoe UI", 14, "bold"),
            bg=color,
            fg="#101828",
            activebackground="#d0d5dd",
            relief="flat",
            width=6,
            height=2,
            cursor="hand2",
        )
        button.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            sticky="nsew",
            padx=3,
            pady=3,
        )
        return button

    def choose_color(self):
        selected_color = colorchooser.askcolor(
            color=self.accent_color,
            title="Choose Calculator Color",
            parent=self.root,
        )[1]
        if selected_color:
            self.accent_color = selected_color
            red = int(selected_color[1:3], 16)
            green = int(selected_color[3:5], 16)
            blue = int(selected_color[5:7], 16)
            text_color = "#101828" if (red * 299 + green * 587 + blue * 114) / 1000 >= 140 else "#ffffff"
            for button in self.accent_buttons:
                button.configure(
                    bg=selected_color,
                    activebackground=selected_color,
                    fg=text_color,
                )

    def enter_value(self, value):
        if value == "±":
            if self.waiting_for_number:
                self.display_value.set("-0")
                self.waiting_for_number = False
                self.result_was_shown = False
            elif self.display_value.get() != "Error":
                current = self.display_value.get()
                if current.startswith("-"):
                    self.display_value.set(current[1:])
                else:
                    self.display_value.set("-" + current)
            return

        if self.display_value.get() == "Error" or self.waiting_for_number or self.result_was_shown:
            self.display_value.set("0" if value == "." else value)
            self.waiting_for_number = False
            self.result_was_shown = False
            return

        current = self.display_value.get()
        if value == ".":
            if "." not in current:
                self.display_value.set(current + ".")
        elif current in ("0", "-0"):
            self.display_value.set(("-" if current.startswith("-") else "") + value)
        else:
            self.display_value.set(current + value)

    def choose_operator(self, label):
        operators = {"×": "*", "÷": "/", "%": "%", "//": "//", "xʸ": "**", "+": "+", "-": "-"}
        operator = operators[label]
        try:
            if self.pending_operator and not self.waiting_for_number:
                result = calculate(
                    self.first_number,
                    self.pending_operator,
                    float(self.display_value.get()),
                )
                self.display_value.set(str(result))
                self.first_number = float(result)
            elif not self.pending_operator or not self.waiting_for_number:
                self.first_number = float(self.display_value.get())

            self.pending_operator = operator
            self.waiting_for_number = True
            self.result_was_shown = False
            self.equation_text.set(f"{self.display_value.get()} {label}")
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            self.show_error(str(error))

    def equals(self):
        if not self.pending_operator or self.waiting_for_number:
            self.show_error("Enter a number and an operator before pressing equals.")
            return

        first_text = str(format_result(self.first_number))
        second_text = self.display_value.get()
        operator_symbols = {"*": "×", "/": "÷", "**": "xʸ"}
        operator_text = operator_symbols.get(self.pending_operator, self.pending_operator)
        equation = f"{first_text} {operator_text} {second_text}"

        try:
            result = calculate(
                self.first_number,
                self.pending_operator,
                float(second_text),
            )
            save_to_history(equation, result)
            self.display_value.set(str(result))
            self.equation_text.set(f"{equation} =")
            self.first_number = float(result)
            self.pending_operator = None
            self.waiting_for_number = True
            self.result_was_shown = True
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            self.show_error(str(error))
        except OSError as error:
            self.show_error(f"Could not save calculation history: {error}")

    def show_error(self, message):
        self.display_value.set("Error")
        self.equation_text.set(message)
        self.first_number = None
        self.pending_operator = None
        self.waiting_for_number = True
        self.result_was_shown = False

    def clear(self):
        self.display_value.set("0")
        self.equation_text.set("")
        self.first_number = None
        self.pending_operator = None
        self.waiting_for_number = False
        self.result_was_shown = False

    def show_history(self):
        window = tk.Toplevel(self.root)
        window.title("Calculation History")
        window.resizable(False, False)
        window.configure(padx=12, pady=12)

        history_text = tk.Text(window, width=52, height=14, wrap="word", state="disabled")
        history_text.pack(pady=(0, 10))

        def refresh_history():
            try:
                with open(HISTORY_FILE, "r", encoding="utf-8") as history_file:
                    lines = history_file.readlines()
            except FileNotFoundError:
                lines = []
            except OSError as error:
                messagebox.showerror("History Error", f"Could not read history: {error}", parent=window)
                return

            history_text.configure(state="normal")
            history_text.delete("1.0", tk.END)
            history_text.insert(
                "1.0",
                "".join(reversed(lines)) if lines else "No history yet.",
            )
            history_text.configure(state="disabled")

        def clear_saved_history():
            if not messagebox.askyesno("Clear History", "Delete all saved calculations?", parent=window):
                return
            try:
                with open(HISTORY_FILE, "w", encoding="utf-8"):
                    pass
            except OSError as error:
                messagebox.showerror("History Error", f"Could not clear history: {error}", parent=window)
                return
            refresh_history()

        tk.Button(window, text="Clear History", command=clear_saved_history).pack(side="left")
        tk.Button(window, text="Close", command=window.destroy).pack(side="right")
        refresh_history()


def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
