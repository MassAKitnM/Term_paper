import random
from collections import defaultdict
from tkinter import Tk, Entry, Button, Canvas
from turtle import width


class Disk:
    def __init__(self):
        self.size = 0
        self.color = ""

    def add_size(self, m: int, n: int):
        self.size = m * 10 + n

    def color_gen(self, used_colors: defaultdict):
        self.color = color_generator(used_colors)


def dec_to_hex(a: int):
    result = ""
    arr = ["a", "b", "c", "d", "e", "f"]
    while a // 16 + a % 16 != 0:
        tmp = a % 16
        a //= 16
        if tmp < 10:
            result = str(tmp) + result
        else:
            tmp -= 10
            result = arr[tmp] + result
    return result

# TODO fix it


def color_generator(used_colors: defaultdict):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = "#" + dec_to_hex(r) + dec_to_hex(g) + dec_to_hex(b)
    if color in used_colors:
        return color_generator(used_colors)
    else:
        used_colors[color]
        return color


def ID_parser(n: int):
    arr = []
    while n // 10 + n % 10 != 0:
        tmp = n % 10
        n //= 10
        arr.append(tmp)
    return arr


class Cnt:
    def __init__(self) -> None:
        self.cnt = 0


def start(id):
    towers_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: []
    }
    disk_array = ID_parser(id)
    used_colors = defaultdict(int)

    for i in range(8, 0, -1):
        for j in range(disk_array[i-1]):
            tmp = Disk()
            tmp.color_gen(used_colors)
            tmp.add_size(9 - i, j + 1)
            towers_dict[i].append(tmp)
        towers_dict[i] = towers_dict[i][::-1]
    return towers_dict


def UsualHanoi(n: int, start: int, finish: int, sum_rods: int, tower: list, cnt: Cnt):
    if n <= 0:
        return
    tmp = sum_rods - start - finish
    cnt.cnt += 1
    UsualHanoi(n-1, start, tmp, sum_rods, tower, cnt)
    tower[finish].append(tower[start][-1])
    tower[start].pop(-1)
    UsualHanoi(n-1, tmp, finish, sum_rods, tower, cnt)


id = 70174538  # TODO id grapler


def StartHanoi(th: dict, cnt):
    l = len(th[8])
    UsualHanoi(l, 8, 7, 21, th, cnt)
    for i in range(7, 2, -1):
        l = len(th[i])
        UsualHanoi(l, i, i-1, 3 * i, th, cnt)
    l = len(th[2])
    UsualHanoi(l, 2, 1, 6, th, cnt)


start_th = (start(id))
end_th = start_th
cnt = Cnt()

StartHanoi(end_th, cnt)
# for el in end_th[7]:
#     print(el.size)

window = Tk()
window.title = ("Towers of Hanoi")
window.geometry("1000x1000")
c = Canvas(window, height=1000, width=1000)
c.pack()
c.create_line(100, 700,  900, 700, width=30)
c.create_line(150, 700, 150, 50, width=5)
c.create_line(250, 700, 250, 50, width=5)
c.create_line(350, 700, 350, 50, width=5)
c.create_line(450, 700, 450, 50, width=5)
c.create_line(550, 700, 550, 50, width=5)
c.create_line(650, 700, 650, 50, width=5)
c.create_line(750, 700, 750, 50, width=5)
c.create_line(850, 700, 850, 50, width=5)
for i in range(8, 2, -1):
    cnt = 0
    y = 700
    for j in start_th[i]:
        # print(type(j.color))
        x1 = 50 + 100 - (i + 2) - j.size / 2
        x2 = 50 + 100 - (i + 2) + j.size / 2
        y1 = y - 12 * cnt
        cnt += 1
        y2 = y - 12 * cnt
        c.create_rectangle(x1, y1, x2, y2, fill=j.color)

window.resizable(False, False)

window.mainloop()
