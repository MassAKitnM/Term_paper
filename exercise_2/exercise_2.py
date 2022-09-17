from tkinter import *
from collections import defaultdict
from tkinter import scrolledtext

if __name__ == "__main__":

    class Bank:
        def __init__(self):
            self.clients = defaultdict(int)

        def deposit(self, name: str, money: int):
            self.clients[name] += money

        def withdraw(self, name: str, money: int):
            self.clients[name] -= money

        def balance(self, name: str):
            if name != "":
                return self.clients.get(name, "NO CLIENT")
            return self.clients.items()

        def transfer(self, name1: str, name2: str, money: int):
            self.clients[name1] -= money
            self.clients[name2] += money

        def income(self, p: int):
            for name in self.clients:
                if self.clients[name] > 0:
                    self.clients[name] = int(self.clients[name] * (1 + p/100))

    def clicked_calculate():
        s = str(text.get(1.0, END))
        text_el = s.split('\n')
        lbl_text = ""
        for el in text_el:
            tmp = el.split(' ')
            if tmp[0] == "DEPOSIT":
                bank.deposit(tmp[1], int(tmp[2]))
            elif tmp[0] == "WITHDRAW":
                bank.withdraw(tmp[1], int(tmp[2]))
            elif tmp[0] == "BALANCE":
                if len(tmp) > 1:
                    out = bank.balance(tmp[1])
                    lbl_text += tmp[1] + ' ' + str(out) + '\n'
                else:
                    data = bank.balance("")
                    out = ""
                    for key, value in data:
                        out += key + ' ' + str(value) + '\n'
                    lbl_text += out
            elif tmp[0] == "TRANSFER":
                bank.transfer(tmp[1], tmp[2], int(tmp[3]))
            elif tmp[0] == "INCOME":
                bank.income(int(tmp[1]))
        lbl.configure(text=lbl_text)

    def clicked_clear():
        text.delete(1.0, END)
        lbl.configure(text="need some input")

    bank = Bank()
    bank.deposit("Sidorchuk", 61899)

    window = Tk()
    window.title("Bank")
    window.geometry('600x600')
    lbl_input = Label(window, text="Input:")
    lbl_input.place(x=120, y=0)
    lbl_output = Label(window, text="Output:")
    lbl_output.place(x=433, y=0)
    lbl = Label(window, text="need some input",
                width=39, height=34, bg="#406080", foreground="white", borderwidth=3, relief="solid", anchor=NW, justify="left")
    lbl.place(x=310, y=20)
    text = scrolledtext.ScrolledText(window, width=34, height=32, bg="#406080",
                                     foreground="white", borderwidth=3, relief="solid")
    text.place(x=10, y=20)
    btn_calculate = Button(window, text="Calculate",
                           command=clicked_calculate)
    btn_calculate.place(x=310, y=560)
    btn_clear = Button(window, text="reset text", command=clicked_clear)
    btn_clear.place(x=450, y=560)
    window.mainloop()
