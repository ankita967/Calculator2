import tkinter as tk
import math
import json
import os


# ==========================================
# FILES
# ==========================================

HISTORY_FILE = "history.json"


# ==========================================
# COLORS
# ==========================================

BG_COLOR = "#202124"
DISPLAY_COLOR = "#303134"
NUMBER_COLOR = "#3C4043"
OPERATOR_COLOR = "#5F6368"
EQUAL_COLOR = "#8AB4F8"
CLEAR_COLOR = "#EA4335"
HISTORY_COLOR = "#34A853"
BACKSPACE_COLOR = "#F9AB00"
SCIENTIFIC_COLOR = "#A142F4"

TEXT_COLOR = "#FFFFFF"


# ==========================================
# HISTORY FUNCTIONS
# ==========================================

def load_history():

    if os.path.exists(HISTORY_FILE):

        try:

            with open(HISTORY_FILE, "r") as file:
                return json.load(file)

        except:
            return []

    return []


def save_history():

    with open(HISTORY_FILE, "w") as file:

        json.dump(
            history,
            file,
            indent=4
        )


# Load previous history
history = load_history()


# ==========================================
# MAIN WINDOW
# ==========================================

window = tk.Tk()

window.title("Scientific Calculator")
window.geometry("430x650")
window.resizable(False, False)
window.configure(bg=BG_COLOR)


# ==========================================
# TITLE
# ==========================================

title = tk.Label(
    window,
    text="SCIENTIFIC CALCULATOR",
    font=("Arial", 20, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)

title.pack(pady=(15, 8))


# ==========================================
# DISPLAY
# ==========================================

display = tk.Entry(
    window,
    font=("Arial", 23, "bold"),
    justify="right",
    bg=DISPLAY_COLOR,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    relief="flat"
)

display.pack(
    padx=20,
    pady=8,
    ipady=15,
    fill="x"
)


# ==========================================
# BASIC FUNCTIONS
# ==========================================

def button_click(value):

    display.insert(
        tk.END,
        value
    )


def clear():

    display.delete(
        0,
        tk.END
    )


def backspace():

    current = display.get()

    if current:

        display.delete(
            len(current) - 1,
            tk.END
        )


# ==========================================
# CALCULATE
# ==========================================

def calculate():

    try:

        expression = display.get()

        result = eval(expression)

        calculation = f"{expression} = {result}"

        history.append(calculation)

        # SAVE HISTORY
        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except ZeroDivisionError:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Cannot divide by 0"
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


# ==========================================
# SCIENTIFIC FUNCTIONS
# ==========================================

def square_root():

    try:

        number = float(display.get())

        result = math.sqrt(number)

        calculation = f"√{number} = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def square():

    try:

        number = float(display.get())

        result = number ** 2

        calculation = f"{number}² = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def percentage():

    try:

        number = float(display.get())

        result = number / 100

        calculation = f"{number}% = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def sine():

    try:

        number = float(display.get())

        result = math.sin(
            math.radians(number)
        )

        calculation = f"sin({number}°) = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def cosine():

    try:

        number = float(display.get())

        result = math.cos(
            math.radians(number)
        )

        calculation = f"cos({number}°) = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def tangent():

    try:

        number = float(display.get())

        result = math.tan(
            math.radians(number)
        )

        calculation = f"tan({number}°) = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def logarithm():

    try:

        number = float(display.get())

        result = math.log10(number)

        calculation = f"log({number}) = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def natural_log():

    try:

        number = float(display.get())

        result = math.log(number)

        calculation = f"ln({number}) = {result}"

        history.append(calculation)

        save_history()

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            str(result)
        )

    except:

        display.delete(
            0,
            tk.END
        )

        display.insert(
            0,
            "Invalid"
        )


def insert_pi():

    display.insert(
        tk.END,
        str(math.pi)
    )


# ==========================================
# HISTORY WINDOW
# ==========================================

def show_history():

    history_window = tk.Toplevel(window)

    history_window.title(
        "Calculation History"
    )

    history_window.geometry(
        "430x500"
    )

    history_window.configure(
        bg=BG_COLOR
    )

    title = tk.Label(
        history_window,
        text="CALCULATION HISTORY",
        font=("Arial", 20, "bold"),
        bg=BG_COLOR,
        fg=TEXT_COLOR
    )

    title.pack(
        pady=20
    )

    history_list = tk.Listbox(
        history_window,
        font=("Arial", 15),
        bg=DISPLAY_COLOR,
        fg=TEXT_COLOR,
        selectbackground=EQUAL_COLOR,
        relief="flat",
        width=32,
        height=14
    )

    history_list.pack(
        padx=20,
        pady=10
    )

    if len(history) == 0:

        history_list.insert(
            tk.END,
            "No calculations yet."
        )

    else:

        for calculation in history:

            history_list.insert(
                tk.END,
                calculation
            )


    def clear_history():

        history.clear()

        save_history()

        history_list.delete(
            0,
            tk.END
        )

        history_list.insert(
            tk.END,
            "History cleared."
        )


    clear_history_button = tk.Button(
        history_window,
        text="CLEAR HISTORY",
        font=("Arial", 14, "bold"),
        bg=CLEAR_COLOR,
        fg=TEXT_COLOR,
        relief="flat",
        width=20,
        height=2,
        command=clear_history
    )

    clear_history_button.pack(
        pady=15
    )


# ==========================================
# SCIENTIFIC BUTTON FRAME
# ==========================================

scientific_frame = tk.Frame(
    window,
    bg=BG_COLOR
)

scientific_frame.pack(
    padx=15,
    pady=5
)


# ==========================================
# SCIENTIFIC BUTTONS
# ==========================================

scientific_buttons = [

    ("√", square_root, 0, 0),
    ("x²", square, 0, 1),
    ("%", percentage, 0, 2),
    ("π", insert_pi, 0, 3),

    ("sin", sine, 1, 0),
    ("cos", cosine, 1, 1),
    ("tan", tangent, 1, 2),
    ("log", logarithm, 1, 3),

    ("ln", natural_log, 2, 0)

]


for text, command, row, column in scientific_buttons:

    button = tk.Button(
        scientific_frame,
        text=text,
        font=("Arial", 13, "bold"),
        bg=SCIENTIFIC_COLOR,
        fg=TEXT_COLOR,
        activebackground=SCIENTIFIC_COLOR,
        relief="flat",
        width=7,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4
    )


# ==========================================
# BASIC BUTTON FRAME
# ==========================================

button_frame = tk.Frame(
    window,
    bg=BG_COLOR
)

button_frame.pack(
    padx=15,
    pady=5
)


# ==========================================
# BASIC BUTTONS
# ==========================================

buttons = [

    ("7", 0, 0),
    ("8", 0, 1),
    ("9", 0, 2),
    ("/", 0, 3),

    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("*", 1, 3),

    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("-", 2, 3),

    ("0", 3, 0),
    (".", 3, 1),
    ("=", 3, 2),
    ("+", 3, 3)

]


for text, row, column in buttons:

    if text == "=":

        command = calculate
        button_color = EQUAL_COLOR
        text_color = "#000000"

    elif text in ["/", "*", "-", "+"]:

        command = lambda value=text: button_click(value)
        button_color = OPERATOR_COLOR
        text_color = TEXT_COLOR

    else:

        command = lambda value=text: button_click(value)
        button_color = NUMBER_COLOR
        text_color = TEXT_COLOR


    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18, "bold"),
        bg=button_color,
        fg=text_color,
        activebackground=button_color,
        relief="flat",
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4
    )


# ==========================================
# BACKSPACE
# ==========================================

backspace_button = tk.Button(
    button_frame,
    text="⌫ BACKSPACE",
    font=("Arial", 12, "bold"),
    bg=BACKSPACE_COLOR,
    fg="#000000",
    relief="flat",
    height=2,
    command=backspace
)

backspace_button.grid(
    row=4,
    column=0,
    columnspan=2,
    padx=4,
    pady=7,
    sticky="ew"
)


# ==========================================
# CLEAR
# ==========================================

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 12, "bold"),
    bg=CLEAR_COLOR,
    fg=TEXT_COLOR,
    relief="flat",
    height=2,
    command=clear
)

clear_button.grid(
    row=4,
    column=2,
    columnspan=2,
    padx=4,
    pady=7,
    sticky="ew"
)


# ==========================================
# HISTORY
# ==========================================

history_button = tk.Button(
    window,
    text="📜 HISTORY",
    font=("Arial", 14, "bold"),
    bg=HISTORY_COLOR,
    fg=TEXT_COLOR,
    activebackground="#188038",
    relief="flat",
    height=2,
    command=show_history
)

history_button.pack(
    padx=20,
    pady=8,
    fill="x"
)


# ==========================================
# START APPLICATION
# ==========================================

window.mainloop()