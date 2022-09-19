import random
from collections import defaultdict
import tkinter


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


def HanoiTower(t1: list, t2: list, t3: list, cnt: int, stop_pnt: list):
    # TODO cnt
    pass


def start(id):
    towers_dict = {
        8: [],
        7: [],
        6: [],
        5: [],
        4: [],
        3: [],
        2: [],
        1: []
    }
    disk_array = ID_parser(id)
    used_colors = defaultdict(int)

    for i in range(8, 0, -1):
        for j in range(disk_array[i-1]):
            tmp = Disk()
            tmp.color_gen(used_colors)
            tmp.add_size(i, j + 1)
            towers_dict[i].append(tmp)

    return towers_dict


id = 70174538  # TODO id grapler

start(id)
