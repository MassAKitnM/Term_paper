from tkinter import *
from math import sqrt


class Calculator:
    def __init__(self) -> None:
        self.text_cur = "0"
        self.text_history = ""
        self.text_show = "0"
        self.usual_mod = True
        self.prev = ""
        self.cells = {
            'm_1': 0,
            'm_2': 0,
            'm_3': 0,
            'm_4': 0,
            'm_5': 0,
            'm_6': 0,
        }
        self.value = 0
        self.history = ""
        self.last_value = 0
        self.type = "int"
        self.operation = None


def clicked_digit(d: str):
    if d == '.':
        calc.text_cur += d
    elif calc.text_cur == "0":
        calc.text_cur = d
    else:
        calc.text_cur += d
    calc.text_show = calc.text_cur
    if calc.usual_mod:
        lbl_cur.configure(text=calc.text_show)


def clicked_negative():
    if calc.text_show[0] != '0':
        if calc.text_show[0] == '-':
            calc.text_show = calc.text_show[1::]
        else:
            calc.text_show = '-' + calc.text_show
        calc.text_cur = calc.text_show
        if calc.usual_mod:
            lbl_cur.configure(text=calc.text_show)


def clicked_clear_text():
    calc.text_cur = "0"
    calc.operation = None
    calc.text_history = ""
    calc.text_show = "0"
    if calc.usual_mod:
        lbl_cur.configure(text=calc.text_show)
        lbl_hist.configure(text=calc.text_history)


def clicked_M_S(m_slot: int):
    if calc.text_show[-1] != '.':
        calc.cells[m_slot] = calc.text_show
        calc.text_cur = "0"
        if calc.usual_mod:
            lbl_cur.configure(text=calc.text_show)
    else:
        calc.text_cur = calc.text_show
        clicked_backspace()
        clicked_M_plus(m_slot)


def clicked_M_R(m_slot: int):
    calc.text_show = calc.cells[m_slot]
    calc.text_cur = "0"
    if calc.usual_mod:
        lbl_cur.configure(text=calc.text_show)


def clicked_M_C(m_slot: int):
    calc.cells[m_slot] = 0


def clicked_clear_all():
    clicked_clear_text()
    for key in calc.cells:
        calc.cells[key] = 0


def clicked_backspace():
    if len(calc.text_cur) > 0:
        if len(calc.text_cur) > 1:
            calc.text_cur = calc.text_cur[0: -1]
        else:
            calc.text_cur = "0"
        if calc.text_cur[0] == '-' and len(calc.text_cur) == 2 and calc.text_cur[1] == 0:
            calc.text_cur = "0"
        if calc.text_cur[0] == '-' and len(calc.text_cur) == 1:
            calc.text_cur = "0"
        if calc.text_cur[-1] == '.':
            calc.text_cur = calc.text_cur[0: -1]
    calc.text_show = calc.text_cur
    if calc.usual_mod:
        lbl_cur.configure(text=calc.text_show)


def clicked_plus():
    if calc.operation == "+" and calc.text_cur == "0":
        calc.text_show = calc.prev
        pass
    elif calc.operation != "+":
        calc.operation = "+"
        calc.prev = calc.text_show
        calc.text_cur = "0"
        calc.text_history = f'{calc.text_show} + '
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
    else:
        tmp = round(float(calc.text_cur) + float(calc.prev), 3)
        if tmp % 1 == 0.0:
            calc.text_show = str(int(tmp))
        else:
            calc.text_show = str(tmp)
        calc.prev = calc.text_show
        calc.text_history = f'{calc.text_show} + '
        calc.text_cur = "0"
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
            lbl_cur.configure(text=calc.text_show)


def clicked_minus():
    if calc.operation == "-" and calc.text_cur == "0":
        calc.text_show = calc.prev
        pass
    elif calc.operation != "-":
        calc.operation = "-"
        calc.prev = calc.text_show
        calc.text_cur = "0"
        calc.text_history = f'{calc.text_show} - '
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
    else:
        tmp = round(float(calc.prev) - float(calc.text_cur), 3)
        if tmp % 1 == 0.0:
            calc.text_show = str(int(tmp))
        else:
            calc.text_show = str(tmp)
        calc.prev = calc.text_show
        calc.text_history = f'{calc.text_show} - '
        calc.text_cur = "0"
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
            lbl_cur.configure(text=calc.text_show)


def clicked_miltiply():
    if calc.operation == "*" and calc.text_cur == "0":
        calc.text_show = calc.prev
        pass
    elif calc.operation != "*":
        calc.operation = "*"
        calc.prev = calc.text_show
        calc.text_cur = "0"
        calc.text_history = f'{calc.text_show} * '
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
    else:
        tmp = round(float(calc.prev) * float(calc.text_cur), 3)
        if tmp % 1 == 0.0:
            calc.text_show = str(int(tmp))
        else:
            calc.text_show = str(tmp)
        calc.prev = calc.text_show
        calc.text_history = f'{calc.text_show} * '
        calc.text_cur = "0"
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
            lbl_cur.configure(text=calc.text_show)


def clicked_div():
    if calc.operation == "/" and calc.text_cur == "0":
        calc.text_show = calc.prev
        pass
    elif calc.operation != "/":
        calc.operation = "/"
        calc.prev = calc.text_show
        calc.text_cur = "0"
        calc.text_history = f'{calc.text_show} / '
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
    else:
        tmp = round(float(calc.prev) / float(calc.text_cur), 3)
        if tmp % 1 == 0.0:
            calc.text_show = str(int(tmp))
        else:
            calc.text_show = str(tmp)
        calc.prev = calc.text_show
        calc.text_history = f'{calc.text_show} / '
        calc.text_cur = "0"
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
            lbl_cur.configure(text=calc.text_show)


def clicked_mod():
    if calc.operation == "%" and calc.text_cur == "0":
        calc.text_show = calc.prev
    elif calc.operation != "%":
        calc.operation = "%"
        calc.prev = calc.text_show
        calc.text_cur = "0"
        calc.text_history = f'{calc.text_show} % '
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
    else:
        tmp = round(float(calc.prev) % float(calc.text_cur), 3)
        if tmp % 1 == 0.0:
            calc.text_show = str(int(tmp))
        else:
            calc.text_show = str(tmp)
        calc.prev = calc.text_show
        calc.text_history = f'{calc.text_show} % '
        calc.text_cur = "0"
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
            lbl_cur.configure(text=calc.text_show)


def clicked_pow():
    calc.text_history += f'sqr{calc.text_show}'
    tmp = round(float(calc.text_show) ** 2, 3)
    if tmp % 1 == 0.0:
        calc.text_show = str(int(tmp))
    else:
        calc.text_show = str(tmp)
    calc.text_cur = calc.text_show
    if calc.usual_mod:
        lbl_hist.configure(text=calc.text_history)
        lbl_cur.configure(text=calc.text_show)


def clicked_sqrt():
    calc.text_history += f'sqrt{calc.text_show}'
    tmp = round(sqrt(float(calc.text_show)), 3)
    if tmp % 1 == 0.0:
        calc.text_show = str(int(tmp))
    else:
        calc.text_show = str(tmp)
    calc.text_cur = calc.text_show
    if calc.usual_mod:
        lbl_hist.configure(text=calc.text_history)
        lbl_cur.configure(text=calc.text_show)


def clicked_equal():
    if calc.operation != None:
        tmp = calc.text_cur
        if calc.operation == "+":
            clicked_plus()
        if calc.operation == "-":
            clicked_minus()
        if calc.operation == "*":
            clicked_miltiply()
        if calc.operation == "/":
            clicked_div()
        if calc.operation == "%":
            clicked_mod()
        calc.text_history += f'{tmp}'
        calc.text_cur = tmp
        calc.prev = calc.text_show
        if calc.usual_mod:
            lbl_hist.configure(text=calc.text_history)
            lbl_cur.configure(text=calc.text_show)
    else:
        pass


def clicked_M_plus(m_slot: int):
    calc.operation = "+"
    calc.prev = calc.text_show
    calc.text_cur = calc.cells[m_slot]
    clicked_plus()


def clicked_M_min(m_slot: int):
    calc.operation = "-"
    calc.prev = calc.text_show
    calc.text_cur = calc.cells[m_slot]
    clicked_minus()


calc = Calculator()
window = Tk()
window.resizable(False, False)
window.title("calculator")
window.geometry('322x500')
window.configure(background="black")

lbl_cur = Label(window, width=24, text="0", anchor=E,
                font=("Arial", 17), background="black", foreground="white")
lbl_cur.place(x=2, y=55)
lbl_hist = Label(window, width=34, text="", anchor=E,
                 font=("Arial", 12), background="black", foreground="#778899")
lbl_hist.place(x=2, y=10)
btn_negative = Button(window, text="+/-", width=10, height=3,
                      background="black", foreground="white", font=("Arial", 9), command=clicked_negative)
btn_negative.place(x=0, y=443)
btn_0 = Button(window, text="0", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('0'))
btn_0.place(x=81, y=443)
btn_float = Button(window, text=".", width=10, height=3,
                   background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('.'))
btn_float.place(x=162, y=443)
btn_equal = Button(window, text="=", width=10, height=3,
                   background="#4169E1", foreground="white", font=("Arial", 9), command=clicked_equal)
btn_equal.place(x=242, y=443)
btn_1 = Button(window, text="1", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('1'))
btn_1.place(x=0, y=385)
btn_2 = Button(window, text="2", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('2'))
btn_2.place(x=81, y=385)
btn_3 = Button(window, text="3", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('3'))
btn_3.place(x=162, y=385)
btn_plus = Button(window, text="+", width=10, height=3,
                  background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_plus)
btn_plus.place(x=242, y=385)
btn_4 = Button(window, text="4", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('4'))
btn_4.place(x=0, y=327)
btn_5 = Button(window, text="5", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('5'))
btn_5.place(x=81, y=327)
btn_6 = Button(window, text="6", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('6'))
btn_6.place(x=162, y=327)
btn_min = Button(window, text="-", width=10, height=3,
                 background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_minus)
btn_min.place(x=242, y=327)
btn_7 = Button(window, text="7", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('7'))
btn_7.place(x=0, y=269)
btn_8 = Button(window, text="8", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('8'))
btn_8.place(x=81, y=269)
btn_9 = Button(window, text="9", width=10, height=3,
               background="black", foreground="white", font=("Arial", 9), command=lambda: clicked_digit('9'))
btn_9.place(x=162, y=269)
btn_mult = Button(window, text="X", width=10, height=3,
                  background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_miltiply)
btn_mult.place(x=242, y=269)
btn_mod = Button(window, text="%", width=10, height=3,
                 background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_mod)
btn_mod.place(x=0, y=211)
btn_pow = Button(window, text="x^2", width=10, height=3,
                 background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_pow)
btn_pow.place(x=81, y=211)
btn_sqrt = Button(window, text="√x", width=10, height=3,
                  background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_sqrt)
btn_sqrt.place(x=162, y=211)
btn_div = Button(window, text="÷", width=10, height=3,
                 background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_div)
btn_div.place(x=242, y=211)
btn_extra = Button(window, text="extra", width=10, height=3,
                   background="#2F4F4F", foreground="white", font=("Arial", 9))
btn_extra.place(x=0, y=153)
btn_ce = Button(window, text="CE", width=10, height=3,
                background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_clear_text)
btn_ce.place(x=81, y=153)
btn_c = Button(window, text="CA", width=10, height=3,
               background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_clear_all)
btn_c.place(x=162, y=153)
btn_del = Button(window, text="←", width=10, height=3,
                 background="#2F4F4F", foreground="white", font=("Arial", 9), command=clicked_backspace)
btn_del.place(x=242, y=153)
btn_M0_S = Button(window, text="MS", width=7, height=1,
                  background="black", foreground="white", font=("Arial", 8), relief=FLAT, command=lambda: clicked_M_S(0))
btn_M0_S.place(x=0, y=124)
btn_M0_R = Button(window, text="MR", width=7, height=1,
                  background="black", foreground="white", font=("Arial", 8), relief=FLAT, command=lambda: clicked_M_R(0))
btn_M0_R.place(x=69, y=124)
btn_M0_plus = Button(window, text="M+", width=7, height=1,
                     background="black", foreground="white", font=("Arial", 8), relief=FLAT, command=lambda: clicked_M_plus(0))
btn_M0_plus.place(x=138, y=124)
btn_M0_min = Button(window, text="M-", width=7, height=1,
                    background="black", foreground="white", font=("Arial", 8), relief=FLAT,  command=lambda: clicked_M_min(0))
btn_M0_min.place(x=210, y=124)
btn_M0_C = Button(window, text="MC", width=7, height=1,
                  background="black", foreground="white", font=("Arial", 8), relief=FLAT, command=lambda: clicked_M_C(0))
btn_M0_C.place(x=270, y=124)


window.mainloop()

"""
# diff y = 58
memory - 6
Dms, 10^x,
Pi, tanh, Ln
-------
переводит из десятичного вида в формат в
градусы, минуты, секунды; возведение десяти
в произвольную степень, число Пи, гиперболический тангенс, натуральный логирифм
"""
