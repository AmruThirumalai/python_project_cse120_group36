import tkinter as tk

DEFAULT_FONT_STYLE = ("Arial", 14)

WHITE = "#FFFFFF"
BLUE_GREEN = "#0D98BA"
INK_BLUE = "#006B88"
COBALT_GREEN = "#660000"
VIOLET = "#7F00FF"

calculation = ''


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_box.delete(1.0, "end")
    text_box.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_box.delete(1.0, "end")
        text_box.insert(1.0, calculation)
    except:
        clear_field()
        text_box.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_box.delete(1.0, "end")


calc = tk.Tk()
calc.geometry("300x400")

# row 1
text_box = tk.Text(calc, height=2, width=16, font=("Arial", 24))
text_box.grid(columnspan=6)

# start row 2
but_open = tk.Button(calc, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14),
                     fg=INK_BLUE, bg=WHITE)
but_open.grid(row=2, column=0)
but_close = tk.Button(calc, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14),
                      fg=INK_BLUE, bg=WHITE)
but_close.grid(row=2, column=1)

but_clear = tk.Button(calc, text="CE", command=clear_field, width=5, font=("Arial", 14),
                      fg=INK_BLUE, bg=WHITE)
but_clear.grid(row=2, column=2)

but_delete = tk.Button(calc, text="<=", command=lambda: add_to_calculation(""), width=5, font=("Arial", 14),
                       fg=BLUE_GREEN, bg=WHITE)
but_delete.grid(row=2, column=3)

# end row 2

# start row 3
but_squared = tk.Button(calc, text="x\u00b2", command=lambda: add_to_calculation(""), width=5, font=("Arial", 14),
                        fg=INK_BLUE, bg=WHITE)
but_squared.grid(row=3, column=0)

but_sqrt = tk.Button(calc, text="\u221ax", command=lambda: add_to_calculation(""), width=5, font=("Arial", 14),
                     fg=INK_BLUE, bg=WHITE)
but_sqrt.grid(row=3, column=1)

but_divX = tk.Button(calc, text="1/x", command=lambda: add_to_calculation(""), width=5, font=("Arial", 14),
                     fg="#006B88", bg="#FFFFFF")
but_divX.grid(row=3, column=2)

# button /
but_div = tk.Button(calc, text="\u00F7", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14),
                    fg=COBALT_GREEN, bg=WHITE)
but_div.grid(row=3, column=3)
# end row 3


# start row 4
# number 7
but7 = tk.Button(calc, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but7.grid(row=4, column=0)

# number 8
but8 = tk.Button(calc, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but8.grid(row=4, column=1)

# number 9
but9 = tk.Button(calc, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but9.grid(row=4, column=2)

# button *
but_multi = tk.Button(calc, text="\u00D7", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14),
                      fg=COBALT_GREEN, bg=WHITE)
but_multi.grid(row=4, column=3)
# end row 4

# start row 5
# number 4
but4 = tk.Button(calc, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but4.grid(row=5, column=0)

# number 5
but5 = tk.Button(calc, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but5.grid(row=5, column=1)

# number 6
but6 = tk.Button(calc, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but6.grid(row=5, column=2)

# button -
but_minus = tk.Button(calc, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14),
                      fg=COBALT_GREEN, bg=WHITE)
but_minus.grid(row=5, column=3)

# end row 5

# start row 6
# number 1
but1 = tk.Button(calc, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but1.grid(row=6, column=0)

# number 2
but2 = tk.Button(calc, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but2.grid(row=6, column=1)

# number 3
but3 = tk.Button(calc, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but3.grid(row=6, column=2)

# button +
but_plus = tk.Button(calc, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14),
                     fg=COBALT_GREEN, bg=WHITE)
but_plus.grid(row=6, column=3)

# end row 6

# start row 7
#
but_period = tk.Button(calc, text=".", command= lambda: add_to_calculation("."), width=5, font=("Arial", 14),
                       fg=VIOLET, bg=WHITE)
but_period.grid(row=7, column=0)

# number 0
but0 = tk.Button(calc, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14),
                 fg=VIOLET, bg=WHITE)
but0.grid(row=7, column=1)
but_equals = tk.Button(calc, text="=", command=evaluate_calculation, width=11, font=("Arial", 14),
                       fg=COBALT_GREEN, bg=WHITE)
but_equals.grid(row=7, column=2, columnspan=2)
# end row 7

calc.mainloop()
