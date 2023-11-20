import math

import tkinter as tk

calculation = ''

#==============================
#Math Functions
def ln(x):
    try:
        return math.log(x)
    except:
        return 'Error:Domain'

def log(x):
    try:
        return math.log10(x)
    except:
        return 'Error:Domain'

def logbase(x,y):
    try:
        return math.log(x,y)
    except:
        return 'Error:Domain'

def testprime(n):
    if n <= 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        else:
            return True

def factorial(n):
    try:
        return math.factorial(n)
    except:
        return 'Error:Domain'

def sqrt(n):
    try:
        return math.sqrt(n)
    except:
        return 'Error:Domain'

def reciprocal(n):
        return 1 / n

#End
#==============================

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

# color 1 = 11151c
# color 2 = 212d40
# color 3 = 364156
# color 4 = 7d4e57


calc = tk.Tk()
calc.geometry("1000x800")


# row 1
text_box = tk.Text(calc, height=2, width=20, font=("Arial", 24))
text_box.grid(columnspan=7)

# start row 2
but_percent = tk.Button(calc, text="%", command=lambda: add_to_calculation("%"), width=5, font=("Arial", 14))
but_percent.grid(row=2, column=0)

but_clear = tk.Button(calc, text="CE", command=clear_field, width=5, font=("Arial", 14), bg="#7d4e57", fg="#f1faee")
but_clear.grid(row=2, column=1)

but_delete = tk.Button(calc, text="<=", command=lambda: add_to_calculation(""), width=11, font=("Arial", 14))
but_delete.grid(row=2, column=2, columnspan=2)

but_fac = tk.Button(calc, text='!', command=lambda: add_to_calculation('factorial('), width=5, font=('Arial', 14))
but_fac.grid(row=2, column=4)
# end row 2

# start row 3

but_divX = tk.Button(calc, text="1/x", command=lambda: add_to_calculation("reciprocal("), width=5, font=("Arial", 14))
but_divX.grid(row=3, column=0)

but_xSqr = tk.Button(calc, text="x^2", command=lambda: add_to_calculation(""), width=5, font=("Arial", 14))
but_xSqr.grid(row=3, column=1)

but_sqrt = tk.Button(calc, text="√", command=lambda: add_to_calculation("sqrt("), width=5, font=("Arial", 14))
but_sqrt.grid(row=3, column=2)

# button /
but_div = tk.Button(calc, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
but_div.grid(row=3, column=3)

but_ln = tk.Button(calc, text='ln', command=lambda: add_to_calculation('ln('), width=5, font=('Arial', 14))
but_ln.grid(row=3, column=4)
# end row 3


# start row 4
# number 7
but7 = tk.Button(calc, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
but7.grid(row=4, column=0)

# number 8
but8 = tk.Button(calc, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
but8.grid(row=4, column=1)

# number 9
but9 = tk.Button(calc, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
but9.grid(row=4, column=2)

# button *
but_multi = tk.Button(calc, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
but_multi.grid(row=4, column=3)

btnlog = tk.Button(calc, text='log', command=lambda: add_to_calculation('log('), width=5, font=('Arial', 14))
btnlog.grid(row=4, column=4)
# end row 4

# start row 5
# number 4
but4 = tk.Button(calc, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
but4.grid(row=5, column=0)

# number 5
but5 = tk.Button(calc, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
but5.grid(row=5, column=1)

# number 6
but6 = tk.Button(calc, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
but6.grid(row=5, column=2)

# button -
but_minus = tk.Button(calc, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
but_minus.grid(row=5, column=3)

btnlogbase = tk.Button(calc, text='logb', command=lambda: add_to_calculation('logbase('), width=5, font=('Arial', 14))
btnlogbase.grid(row=5, column=4)
# end row 5

# start row 6
# number 1
but1 = tk.Button(calc, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
but1.grid(row=6, column=0)

# number 2
but2 = tk.Button(calc, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
but2.grid(row=6, column=1)

# number 3
but3 = tk.Button(calc, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
but3.grid(row=6, column=2)

# button +
but_plus = tk.Button(calc, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
but_plus.grid(row=6, column=3)


btnpi = tk.Button(calc, text='π', command=lambda: add_to_calculation(math.pi), width=5, font=('Arial', 14))
btnpi.grid(row=6, column=4)

btnprime = tk.Button(calc, text='prime', command=lambda: add_to_calculation('testprime('), width=5, font=('Arial', 14))
but_prime.grid(row=6, column=5)
# end row 6

# start row 7
#
but_open = tk.Button(calc, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
but_open.grid(row=7, column=0)

# number 0
but0 = tk.Button(calc, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
but0.grid(row=7, column=1)

but_close = tk.Button(calc, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
but_close.grid(row=7, column=2)

but_equals = tk.Button(calc, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
but_equals.grid(row=7, column=3)

but_e = tk.Button(calc, text='e', command=lambda: add_to_calculation(math.e), width=5, font=('Arial', 14))
but_e.grid(row=7, column=4)

btncomma = tk.Button(calc, text=',', command=lambda: add_to_calculation(','), width=5, font=('Arial', 14))
btncomma.grid(row=7, column=5)
# end row 7

calc.mainloop()
