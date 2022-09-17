from tkinter import *
from collections import defaultdict

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

    def clicked():
        s = ent.get()
        text_el = s.split()
        lbl.configure(text=s)
        if text_el[0] == "DEPOSIT":
            bank.deposit(text_el[1], int(text_el[2]))
            lbl.configure(text="COMMAND ACCEPT, INPUT NEXT COMAND")
        elif text_el[0] == "WITHDRAW":
            bank.withdraw(text_el[1], int(text_el[2]))
            lbl.configure(text="COMMAND ACCEPT, INPUT NEXT COMAND")
        elif text_el[0] == "BALANCE":
            if len(text_el) > 1:
                tmp = bank.balance(text_el[1])
            else:
                tmp = bank.balance("")
                tmp2 = ""
                for key, value in tmp:
                    tmp2 += key + ' ' + str(value) + '\n'
            lbl.configure(text=tmp2)
        elif text_el[0] == "TRANSFER":
            bank.transfer(text_el[1], text_el[2], int(text_el[3]))
            lbl.configure(text="COMMAND ACCEPT, INPUT NEXT COMAND")
        elif text_el[0] == "INCOME":
            bank.income(int(text_el[1]))
            lbl.configure(text="COMMAND ACCEPT, INPUT NEXT COMAND")
        else:
            lbl.configure(text=text_el[0])

    bank = Bank()
    bank.deposit("Sidorchuk", 61899)

    window = Tk()
    window.title("Bank")
    window.geometry('600x250')
    lbl = Label(window, text="need some input")
    ent = Entry(window, width=100)
    ent.grid(column=0, row=0)
    lbl.grid(column=0, row=3)
    btn = Button(window, text="Calculate", command=clicked)
    btn.grid(column=0, row=1)
    window.mainloop()
