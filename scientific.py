import math

import tkinter as tk

from decimal import Decimal

from fractions import Fraction

import ast

DEFAULT_FONT_STYLE = ("Arial", 14)

WHITE = "#FFFFFF"
BLUE_GREEN = "#0D98BA"
INK_BLUE = "#006B88"
MAROON = "#660000"
VIOLET = "#7F00FF"
EMERALD_GREEN = "#287233"
BLUE_LILAC = "#6C4675"
PEARL_PINK = "#B44C43"
PEARL_VIOLET = "#8673A1"
MIDNIGHT_BLUE = "#191970"
DEEP_TEAL = "#033E3E"
AZTECH_PURPLE = "#893BFF"

calculation = ''

calcstate = 'Scientific'

# ==============================
# Math Functions
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


def logbase(x, y):
    try:
        return math.log(x, y)
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
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True


def factorial(n):
    if str(int(n)) == str(n):
        n = int(n)
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
    return Fraction(1, n)


def frac_to_dec(x):
    try:
        return Decimal(x)
    except:
        return 'Error:Domain'


def dec_to_frac(x):
    try:
        return Fraction(x)
    except:
        return 'Error:Domain'


def absou(x):
    try:
        return math.fabs(x)
    except:
        return 'Error:Domain'


def square_random_number(x, y):
    try:
        return pow(x, y)
    except:
        return 'Error:Domain'


def binary(x):
    binval = bin(x)
    binval = binval[2:]
    return binval


def octal(x):
    octval = oct(x)
    octval = octval[2:]
    return octval


def sqr(x):
    return x ** 2


def radian(x):
    return math.radians(x)


def sin(x):
    if x % math.pi == 0:
        return 0.0
    else:
        return math.sin(x)

def cos(x):
    if x % (math.pi / 2) == 0 and x % math.pi != 0:
        return 0.0
    else:
        return math.cos(x)

def tan(x):
    if x % math.pi == 0:
        return 0.0
    elif x % (math.pi / 2) == 0:
        return 'undefined'
    else:
        return math.tan(x)

def arcsin(x):
    return math.asin(x)

def arccos(x):
    return math.acos(x)

def arctan(x):
    return math.atan(x)

# End
# ==============================
def construct_decimal_node(value):
    return ast.Call(
        func = ast.Name(id="Decimal", ctx=ast.Load()),
        args = [ast.Str(str(value.n))],
        keywords = []
    )
    #return expr

class FloatLiteralReplacer(ast.NodeTransformer):
    def visit_Num(self, node):
        return construct_decimal_node(node)

def check_parentheses():
    global calculation
    calculation = str(calculation)
    calc_list = list(calculation)
    open_count = calc_list.count('(')
    close_count = calc_list.count(')')
    while open_count > close_count:
        calculation = calculation + ')'
        close_count += 1
    return calculation

def eval_state_define():
    global calculation
    eval_state = ''
    check_parentheses()
    i = .99999
    y = str(calculation)
    print(y)
    try:
        if eval(y) <= 1.0 and eval(y) > i:
            eval_state = '1'
        else:
            eval_state = '2'
    except:
        eval_state = '2'
    return eval_state

def add_to_calculation(symbol):
    global calculation
    calculation = str(calculation)
    calculation += str(symbol)
    text_box.delete(1.0, "end")
    text_box.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    eval_state = eval_state_define()
    try:
        if eval_state == '1':
            check_parentheses()
            calculation = str(eval(calculation))
            text_box.delete(1.0, "end")
            text_box.insert(1.0, calculation)
        else:
            try:
                check_parentheses()
                node = ast.parse(calculation, mode="eval")
                node = FloatLiteralReplacer().visit(node)
                ast.fix_missing_locations(node)  # add diagnostic information to the nodes we created
                code = compile(node, filename="", mode="eval")
                calculation = eval(code)
                text_box.delete(1.0, "end")
                text_box.insert(1.0, calculation)
            except:
                check_parentheses()
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

def backspace():
    global calculation
    calculation = calculation[:-1]
    text_box.delete('end-2c')


def store():
    global calculation
    global memhold
    memhold = ''
    memhold = calculation


def memory():
    global calculation
    global memhold
    add_to_calculation(memhold)

def standard():
    try:
        global calcstate
        calcstate = 'Standard'
        print(calcstate)
        return calcstate
    finally:
        calc.destroy()


def scientific():
    try:
        global calcstate
        calcstate = 'Scientific'
        print(calcstate)
        return calcstate
    finally:
        calc.destroy()

def exit():
    try:
        global calcstate
        calcstate = 'exit'
        print(calcstate)
        return calcstate
    finally:
        calc.destroy()
while calcstate != 'exit':
    if calcstate == 'Scientific':
        #This is the scientific Calculator
        calc = tk.Tk()
        calc.geometry("575x350")

        # row 1
        text_box = tk.Text(calc, height=2, width=30, font=("Arial", 24))
        text_box.grid(columnspan=8)

        # start row 2
        but_exit = tk.Button(calc, text="exit", command=exit, width=5, font=DEFAULT_FONT_STYLE,
                                fg=INK_BLUE, bg=WHITE)
        but_exit.grid(row=2, column=0)

        but_clear = tk.Button(calc, text="CE", command=clear_field, width=5, font=DEFAULT_FONT_STYLE,
                              fg=INK_BLUE, bg=WHITE)
        but_clear.grid(row=2, column=1)

        but_delete = tk.Button(calc, text="⌫", command=backspace, width=11, font=DEFAULT_FONT_STYLE,
                               fg=BLUE_GREEN, bg=WHITE)
        but_delete.grid(row=2, column=2, columnspan=2)

        but_e = tk.Button(calc, text='e', command=lambda: add_to_calculation(math.e), width=5, font=DEFAULT_FONT_STYLE,
                          fg=EMERALD_GREEN, bg=WHITE)
        but_e.grid(row=2, column=4)

        but_dec_to_frac = tk.Button(calc, text="d→f", command=lambda: add_to_calculation("dec_to_frac("), width=5,
                                    font=DEFAULT_FONT_STYLE, fg=EMERALD_GREEN, bg=WHITE)
        but_dec_to_frac.grid(row=2, column=5)

        but_rad = tk.Button(calc, text='rad', command=lambda: add_to_calculation("radian("), width=5,
                            font=DEFAULT_FONT_STYLE, 
                            fg=DEEP_TEAL, bg=WHITE)
        but_rad.grid(row=2, column=6)

        but_fac = tk.Button(calc, text='!', command=lambda: add_to_calculation('factorial('), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=EMERALD_GREEN, bg=WHITE)
        but_fac.grid(row=2, column=7)
        # end row 2

        # start row 3

        but_divX = tk.Button(calc, text="1/x", command=lambda: add_to_calculation("reciprocal("), width=5,
                             font=DEFAULT_FONT_STYLE,
                             fg=INK_BLUE, bg=WHITE)
        but_divX.grid(row=3, column=0)

        but_xSqr = tk.Button(calc, text="x²", command=lambda: add_to_calculation("sqr("), width=5, 
                             font=DEFAULT_FONT_STYLE,
                             fg=INK_BLUE, bg=WHITE)
        but_xSqr.grid(row=3, column=1)

        but_sqrt = tk.Button(calc, text="√", command=lambda: add_to_calculation("sqrt("), width=5, 
                             font=DEFAULT_FONT_STYLE,
                             fg=EMERALD_GREEN, bg=WHITE)
        but_sqrt.grid(row=3, column=2)

        # button /
        but_div = tk.Button(calc, text="/", command=lambda: add_to_calculation("/"), width=5, font=DEFAULT_FONT_STYLE,
                            fg=MAROON, bg=WHITE)
        but_div.grid(row=3, column=3)

        but_ln = tk.Button(calc, text='ln', command=lambda: add_to_calculation('ln('), width=5, font=DEFAULT_FONT_STYLE,
                           fg=PEARL_PINK, bg=WHITE)
        but_ln.grid(row=3, column=4)

        but_abs = tk.Button(calc, text="abs", command=lambda: add_to_calculation('absou('), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=PEARL_PINK, bg=WHITE)
        but_abs.grid(row=3, column=5)

        but_store = tk.Button(calc, text='store', command=store, width=5, font=DEFAULT_FONT_STYLE, 
                              fg=MIDNIGHT_BLUE, bg=WHITE)
        but_store.grid(row=3, column=6)

        but_stan = tk.Button(calc, text='stan', command=standard, width=5, font=DEFAULT_FONT_STYLE,
                             fg=AZTECH_PURPLE, bg=WHITE)
        but_stan.grid(row=3, column=7)
        # end row 3

        # start row 4
        # number 7
        but7 = tk.Button(calc, text="7", command=lambda: add_to_calculation(7), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but7.grid(row=4, column=0)

        # number 8
        but8 = tk.Button(calc, text="8", command=lambda: add_to_calculation(8), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but8.grid(row=4, column=1)

        # number 9
        but9 = tk.Button(calc, text="9", command=lambda: add_to_calculation(9), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but9.grid(row=4, column=2)

        # button *
        but_multi = tk.Button(calc, text="*", command=lambda: add_to_calculation("*"), width=5, font=DEFAULT_FONT_STYLE,
                              fg=MAROON, bg=WHITE)
        but_multi.grid(row=4, column=3)

        but_log = tk.Button(calc, text='log', command=lambda: add_to_calculation('log('), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=PEARL_PINK, bg=WHITE)
        but_log.grid(row=4, column=4)

        but_oct = tk.Button(calc, text='oct', command=lambda: add_to_calculation('octal('), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=PEARL_VIOLET, bg=WHITE)
        but_oct.grid(row=4, column=5)

        but_mem = tk.Button(calc, text='mem', command=memory, width=5, font=DEFAULT_FONT_STYLE,
                            fg=MIDNIGHT_BLUE, bg=WHITE)
        but_mem.grid(row=4, column=6)

        but_sci = tk.Button(calc, text='sci', command=scientific, width=5, font=DEFAULT_FONT_STYLE,
                            fg=AZTECH_PURPLE, bg=WHITE)
        but_sci.grid(row=4, column=7)
        # end row 4

        # start row 5
        # number 4
        but4 = tk.Button(calc, text="4", command=lambda: add_to_calculation(4), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but4.grid(row=5, column=0)

        # number 5
        but5 = tk.Button(calc, text="5", command=lambda: add_to_calculation(5), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but5.grid(row=5, column=1)

        # number 6
        but6 = tk.Button(calc, text="6", command=lambda: add_to_calculation(6), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but6.grid(row=5, column=2)

        # button -
        but_minus = tk.Button(calc, text="-", command=lambda: add_to_calculation("-"), width=5, font=DEFAULT_FONT_STYLE,
                              fg=MAROON, bg=WHITE)
        but_minus.grid(row=5, column=3)

        but_logbase = tk.Button(calc, text='logb', command=lambda: add_to_calculation('logbase('), width=5,
                                font=DEFAULT_FONT_STYLE,
                                fg=PEARL_PINK, bg=WHITE)
        but_logbase.grid(row=5, column=4)

        but_bin = tk.Button(calc, text='bin', command=lambda: add_to_calculation('binary('), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=PEARL_VIOLET, bg=WHITE)
        but_bin.grid(row=5, column=5)

        but_sin = tk.Button(calc, text='sin', command=lambda: add_to_calculation('sin('), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=DEEP_TEAL, bg=WHITE)
        but_sin.grid(row=5, column=6)

        but_asin = tk.Button(calc, text='asin', command=lambda: add_to_calculation('arcsin('), width=5, 
                             font=DEFAULT_FONT_STYLE,
                             fg=DEEP_TEAL, bg=WHITE)
        but_asin.grid(row=5, column=7)
        # end row 5

        # start row 6
        # number 1
        but1 = tk.Button(calc, text="1", command=lambda: add_to_calculation(1), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but1.grid(row=6, column=0)

        # number 2
        but2 = tk.Button(calc, text="2", command=lambda: add_to_calculation(2), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but2.grid(row=6, column=1)

        # number 3
        but3 = tk.Button(calc, text="3", command=lambda: add_to_calculation(3), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but3.grid(row=6, column=2)

        # button +
        but_plus = tk.Button(calc, text="+", command=lambda: add_to_calculation("+"), width=5, font=DEFAULT_FONT_STYLE,
                             fg=MAROON, bg=WHITE)
        but_plus.grid(row=6, column=3)

        but_pi = tk.Button(calc, text='π', command=lambda: add_to_calculation(math.pi), width=5, 
                           font=DEFAULT_FONT_STYLE,
                           fg=EMERALD_GREEN, bg=WHITE)
        but_pi.grid(row=6, column=4)

        but_prime = tk.Button(calc, text='prime', command=lambda: add_to_calculation('testprime('), width=5,
                              font=DEFAULT_FONT_STYLE,
                              fg=PEARL_PINK, bg=WHITE)
        but_prime.grid(row=6, column=5)

        but_cos = tk.Button(calc, text='cos', command=lambda: add_to_calculation('cos('), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=DEEP_TEAL, bg=WHITE)
        but_cos.grid(row=6, column=6)

        but_acos = tk.Button(calc, text='acos', command=lambda: add_to_calculation('arccos('), width=5, 
                             font=DEFAULT_FONT_STYLE,
                             fg=DEEP_TEAL, bg=WHITE)
        but_acos.grid(row=6, column=7)
        # end row 6

        # start row 7
        #

        # number 0
        but_period = tk.Button(calc, text=".", command=lambda: add_to_calculation("."), width=5, 
                               font=DEFAULT_FONT_STYLE,
                               fg=VIOLET, bg=WHITE)
        but_period.grid(row=7, column=0)

        but_comma = tk.Button(calc, text=',', command=lambda: add_to_calculation(','), width=5, font=DEFAULT_FONT_STYLE,
                              fg=BLUE_LILAC, bg=WHITE)
        but_comma.grid(row=7, column=1)

        but0 = tk.Button(calc, text="0", command=lambda: add_to_calculation(0), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but0.grid(row=7, column=2)

        but_equals = tk.Button(calc, text="=", command=evaluate_calculation, width=5, font=DEFAULT_FONT_STYLE,
                               fg=MAROON, bg=WHITE)
        but_equals.grid(row=7, column=3)

        but_open = tk.Button(calc, text="(", command=lambda: add_to_calculation("("), width=5, font=DEFAULT_FONT_STYLE,
                             fg=INK_BLUE, bg=WHITE)
        but_open.grid(row=7, column=4)

        but_close = tk.Button(calc, text=")", command=lambda: add_to_calculation(")"), width=5, font=DEFAULT_FONT_STYLE,
                              fg=INK_BLUE, bg=WHITE)
        but_close.grid(row=7, column=5)

        but_tan = tk.Button(calc, text="tan", command=lambda: add_to_calculation("tan("), width=5, 
                            font=DEFAULT_FONT_STYLE,
                            fg=DEEP_TEAL, bg=WHITE)
        but_tan.grid(row=7, column=6)

        but_atan = tk.Button(calc, text="atan", command=lambda: add_to_calculation("arctan("), width=5, 
                             font=DEFAULT_FONT_STYLE,
                             fg=DEEP_TEAL, bg=WHITE)
        but_atan.grid(row=7, column=7)

        # end row 7

        calc.mainloop()

    if calcstate == ('Standard'):
        calc = tk.Tk()
        calc.geometry("300x400")

        # row 1
        text_box = tk.Text(calc, height=2, width=16, font=("Arial", 24))
        text_box.grid(columnspan=6)

        # start row 2
        but_open = tk.Button(calc, text="(", command=lambda: add_to_calculation("("), width=5, font=DEFAULT_FONT_STYLE,
                             fg=INK_BLUE, bg=WHITE)
        but_open.grid(row=2, column=0)
        but_close = tk.Button(calc, text=")", command=lambda: add_to_calculation(")"), width=5, font=DEFAULT_FONT_STYLE,
                              fg=INK_BLUE, bg=WHITE)
        but_close.grid(row=2, column=1)

        but_clear = tk.Button(calc, text="CE", command=clear_field, width=5, font=DEFAULT_FONT_STYLE,
                              fg=INK_BLUE, bg=WHITE)
        but_clear.grid(row=2, column=2)

        but_delete = tk.Button(calc, text="⌫", command=backspace, width=5, font=DEFAULT_FONT_STYLE,
                               fg=BLUE_GREEN, bg=WHITE)
        but_delete.grid(row=2, column=3)

        # end row 2

        # start row 3
        but_squared = tk.Button(calc, text="x\u00b2", command=lambda: add_to_calculation("sqr("), width=5,
                                font=DEFAULT_FONT_STYLE,
                                fg=INK_BLUE, bg=WHITE)
        but_squared.grid(row=3, column=0)

        but_sqrt = tk.Button(calc, text="\u221ax", command=lambda: add_to_calculation("sqrt("), width=5,
                             font=DEFAULT_FONT_STYLE,
                             fg=INK_BLUE, bg=WHITE)
        but_sqrt.grid(row=3, column=1)

        but_divX = tk.Button(calc, text="1/x", command=lambda: add_to_calculation("reciprocal("), width=5,
                             font=DEFAULT_FONT_STYLE,
                             fg=INK_BLUE, bg=WHITE)
        but_divX.grid(row=3, column=2)

        # button /
        but_div = tk.Button(calc, text="\u00F7", command=lambda: add_to_calculation("/"), width=5,
                            font=DEFAULT_FONT_STYLE,
                            fg=MAROON, bg=WHITE)
        but_div.grid(row=3, column=3)
        # end row 3

        # start row 4
        # number 7
        but7 = tk.Button(calc, text="7", command=lambda: add_to_calculation(7), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but7.grid(row=4, column=0)

        # number 8
        but8 = tk.Button(calc, text="8", command=lambda: add_to_calculation(8), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but8.grid(row=4, column=1)

        # number 9
        but9 = tk.Button(calc, text="9", command=lambda: add_to_calculation(9), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but9.grid(row=4, column=2)

        # button *
        but_multi = tk.Button(calc, text="\u00D7", command=lambda: add_to_calculation("*"), width=5,
                              font=DEFAULT_FONT_STYLE,
                              fg=MAROON, bg=WHITE)
        but_multi.grid(row=4, column=3)
        # end row 4

        # start row 5
        # number 4
        but4 = tk.Button(calc, text="4", command=lambda: add_to_calculation(4), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but4.grid(row=5, column=0)

        # number 5
        but5 = tk.Button(calc, text="5", command=lambda: add_to_calculation(5), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but5.grid(row=5, column=1)

        # number 6
        but6 = tk.Button(calc, text="6", command=lambda: add_to_calculation(6), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but6.grid(row=5, column=2)

        # button -
        but_minus = tk.Button(calc, text="-", command=lambda: add_to_calculation("-"), width=5, font=DEFAULT_FONT_STYLE,
                              fg=MAROON, bg=WHITE)
        but_minus.grid(row=5, column=3)

        # end row 5

        # start row 6
        # number 1
        but1 = tk.Button(calc, text="1", command=lambda: add_to_calculation(1), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but1.grid(row=6, column=0)

        # number 2
        but2 = tk.Button(calc, text="2", command=lambda: add_to_calculation(2), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but2.grid(row=6, column=1)

        # number 3
        but3 = tk.Button(calc, text="3", command=lambda: add_to_calculation(3), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but3.grid(row=6, column=2)

        # button +
        but_plus = tk.Button(calc, text="+", command=lambda: add_to_calculation("+"), width=5, font=DEFAULT_FONT_STYLE,
                             fg=MAROON, bg=WHITE)
        but_plus.grid(row=6, column=3)

        # end row 6

        # start row 7
        #
        but_period = tk.Button(calc, text=".", command=lambda: add_to_calculation("."), width=5,
                               font=DEFAULT_FONT_STYLE,
                               fg=VIOLET, bg=WHITE)
        but_period.grid(row=7, column=0)

        # number 0
        but0 = tk.Button(calc, text="0", command=lambda: add_to_calculation(0), width=5, font=DEFAULT_FONT_STYLE,
                         fg=VIOLET, bg=WHITE)
        but0.grid(row=7, column=1)
        but_equals = tk.Button(calc, text="=", command=evaluate_calculation, width=11, font=DEFAULT_FONT_STYLE,
                               fg=MAROON, bg=WHITE)
        but_equals.grid(row=7, column=2, columnspan=2)
        # end row 7
        
        # start row 8
        but_exit = tk.Button(calc, text='exit', command=exit, width=5, font=DEFAULT_FONT_STYLE,
                             fg=PEARL_PINK, bg=WHITE)
        but_exit.grid(row=8, column=0)

        but_sci = tk.Button(calc, text='sci', command=scientific, width=5, font=DEFAULT_FONT_STYLE, 
                            fg=AZTECH_PURPLE, bg=WHITE)
        but_sci.grid(row=8, column=1)

        but_store = tk.Button(calc, text='store', command=store, width=5, font=DEFAULT_FONT_STYLE, 
                              fg=MIDNIGHT_BLUE, bg=WHITE)
        but_store.grid(row=8, column=2)

        but_mem = tk.Button(calc, text='mem', command=memory, width=5, font=DEFAULT_FONT_STYLE, 
                            fg=MIDNIGHT_BLUE, bg=WHITE)
        but_mem.grid(row=8, column=3)
        # end row 8
        calc.mainloop()
