import random
from collections import defaultdict
from tkinter import Tk, Entry, Button, Canvas, messagebox, Label
from copy import deepcopy
from enum import Enum
import time

ANIMATION_TOTAL_MOVES = 1
ANIMATION_STAGE_LENGTH = 60
GOING_UP_Y = 150
DISK_HEIGHT = 12
DISPLAY_EVERY_N_SEC = 1
CHECK_TIME_EVERY = 5e5


class TKState:
    def __init__(self):
        pass


tkState = TKState()


class AnimationState(Enum):
    GOING_UP = 0
    GOING_SIDEWAYS = 1
    GOING_DOWN = 2


def _linear(a, b, percent):
    return (a + (b - a) * percent)


class Animation:
    def __init__(self, disk, x, y, dx, dy):
        self.stage = AnimationState.GOING_UP
        self.progress = 0
        self.partial = False
        self.disk = disk
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def tick(self):
        self.progress += 1
        if self.partial and self.stage == AnimationState.GOING_SIDEWAYS and self.progress >= ANIMATION_STAGE_LENGTH / 2:
            return True
        if self.progress >= ANIMATION_STAGE_LENGTH:
            self.progress = 0
            if self.stage == AnimationState.GOING_DOWN:
                return True
            self.stage = AnimationState(self.stage.value + 1)
        return False

    def percent(self):
        return self.progress / ANIMATION_STAGE_LENGTH

    def _get_current_coords(self):
        if self.stage == AnimationState.GOING_SIDEWAYS:
            x = _linear(self.x, self.dx, self.percent())
        elif self.stage == AnimationState.GOING_UP:
            x = self.x
        else:
            x = self.dx
        if self.stage == AnimationState.GOING_UP:
            y = _linear(self.y, GOING_UP_Y, self.percent())
        elif self.stage == AnimationState.GOING_SIDEWAYS:
            y = GOING_UP_Y
        else:
            y = _linear(GOING_UP_Y, self.dy, self.percent())
        return x, y

    def draw(self, canvas):
        x, y = self._get_current_coords()
        self.disk.draw(canvas, x, y)


class Disk:
    def __init__(self):
        self.size = 0
        self.color = ""

    def add_size(self, m: int, n: int):
        self.size = m * 10 + n

    def color_gen(self, used_colors: defaultdict):
        self.color = color_generator(used_colors)

    def draw(self, canvas, x, y):
        canvas.create_rectangle(x - self.size / 2, y, x +
                                self.size / 2, y + DISK_HEIGHT, fill=self.color)
        canvas.create_text(x, y + 6, text=str(self.size))


class Cnt:
    def __init__(self) -> None:
        self.cnt = 0


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
    if len(result) == 1:
        result = '0' + result
    return result


def color_generator(used_colors: defaultdict):
    r = random.randint(3, 255)
    g = random.randint(3, 255)
    b = random.randint(3, 255)
    color = "#" + dec_to_hex(r) + dec_to_hex(g) + dec_to_hex(b)
    if color in used_colors:
        return color_generator(used_colors)
    else:
        used_colors[color]
        return color


def ID_parser(id: str):
    return list(map(int, id))[::-1]


def CreateTower(id):
    towers = [[] for _ in range(9)]
    disk_array = ID_parser(id)
    used_colors = defaultdict(int)

    for i in range(8, 0, -1):
        for j in range(disk_array[i-1]):
            tmp = Disk()
            tmp.color_gen(used_colors)
            tmp.add_size(9 - i, j + 1)
            towers[i].append(tmp)
        towers[i] = towers[i][::-1]
    return towers


def draw_frame(canvas, tower, animation):
    canvas.delete("all")

    canvas.create_line(100, 700,  900, 700, width=30)
    canvas.create_line(150, 700, 150, 350, width=5)
    canvas.create_line(250, 700, 250, 350, width=5)
    canvas.create_line(350, 700, 350, 350, width=5)
    canvas.create_line(450, 700, 450, 350, width=5)
    canvas.create_line(550, 700, 550, 350, width=5)
    canvas.create_line(650, 700, 650, 350, width=5)
    canvas.create_line(750, 700, 750, 350, width=5)
    canvas.create_line(850, 700, 850, 350, width=5)

    for i in range(8, 0, -1):
        cnt = 0
        y = 685
        for j in tower[i]:
            j.draw(canvas, 150 + 100 * (8 - i), y - DISK_HEIGHT * (cnt + 1))
            cnt += 1

    if animation is not None:
        animation.draw(canvas)
    canvas.update()


display_cnt = 0
last_display_time = 0


def usual_hanoi(n: int, start: int, finish: int, sum_rods: int, tower: list, cnt: Cnt, canvas, stop, results):
    global display_cnt, last_display_time
    if n <= 0:
        return
    tmp = sum_rods - start - finish
    usual_hanoi(n-1, start, tmp, sum_rods, tower, cnt, canvas, stop, results)
    cnt.cnt += 1
    tower[finish].append(tower[start][-1])
    tower[start].pop(-1)
    display_cnt += 1
    if display_cnt >= CHECK_TIME_EVERY:
        if time.time() - last_display_time >= DISPLAY_EVERY_N_SEC:
            draw_frame(canvas, tower, None)
            last_display_time = time.time()
        display_cnt = 0

    for stopPoint in stop:
        if cnt.cnt >= stopPoint - ANIMATION_TOTAL_MOVES and cnt.cnt <= stopPoint:
            results[stopPoint].append(
                (deepcopy(tower), start, finish, tower[finish][-1]))

    usual_hanoi(n-1, tmp, finish, sum_rods, tower, cnt, canvas, stop, results)


def start_hanoi(th: list, cnt, canvas, recordIterations):
    stop = []
    results = None
    if recordIterations:
        stop = tkState.stop
        results = defaultdict(list)
    l = len(th[8])
    usual_hanoi(l, 8, 7, 21, th, cnt, canvas, stop, results)
    for i in range(7, 2, -1):
        l = len(th[i])
        usual_hanoi(l, i, i-1, 3 * i, th, cnt, canvas, stop, results)
    l = len(th[2])
    usual_hanoi(l, 2, 1, 6, th, cnt, canvas, stop, results)
    draw_frame(canvas, th, None)
    return results


def draw_animation(canvas, towerList, isPartial):
    for i in range(0, len(towerList)):
        curTower, start, finish, disk = towerList[i]
        curTower = deepcopy(curTower)
        curTower[finish].pop(-1)
        if isPartial and i + 1 == len(towerList):
            animation = Animation(
                disk, 150 + 100 * (8 - start), 685 - DISK_HEIGHT * (len(curTower[start]) + 1), 150 + 100 * (8 - finish), 685 - DISK_HEIGHT * (len(curTower[finish]) + 1))
            animation.partial = True
        else:
            animation = Animation(
                disk, 150 + 100 * (8 - start), 685 - DISK_HEIGHT * (len(curTower[start]) + 1), 150 + 100 * (8 - finish), 685 - DISK_HEIGHT * (len(curTower[finish]) + 1))
        while True:
            draw_frame(canvas, curTower, animation)
            if animation.tick():
                curTower[finish].append(disk)
                if not animation.partial:
                    draw_frame(canvas, curTower, None)
                break


def setup_tk():
    def tk_start():
        id = ''
        for e in entities:
            id += e.get()
        if not id.isnumeric() or len(id) != 8:
            messagebox.showerror('Error', 'Specify correct id')
            return

        tkState.stop = []
        tkState.isPartial = []

        tkState.percentage = []
        for e in entities:
            text = e.get()
            if len(text) != 2:
                messagebox.showerror('Error', 'Specify correct id block')
                return
            tkState.percentage.append(int(text))

        btn_start['state'] = 'disabled'
        for e in entities:
            e['state'] = 'disabled'

        tkState.tower = CreateTower(id)
        tkState.cnt = Cnt()
        start_hanoi(deepcopy(tkState.tower), tkState.cnt, canvas, False)

        for p in tkState.percentage:
            isPartial = not (tkState.cnt.cnt / 100 * p).is_integer()
            it = tkState.cnt.cnt // 100 * p + isPartial
            tkState.stop.append(it)
            tkState.isPartial.append(isPartial)
        tkState.stop.append(tkState.cnt.cnt)
        tkState.isPartial.append(False)

        tkState.results = start_hanoi(
            deepcopy(tkState.tower), Cnt(), canvas, True)
        iteration_count['text'] = str(tkState.cnt.cnt) + ' iterations'

        for button in solve_buttons:
            button['state'] = 'normal'

    def tk_draw_animation(stopIndex):
        if stopIndex >= len(tkState.percentage):
            iteration_count['text'] = str(tkState.cnt.cnt) + ' iterations'
        else:
            p = tkState.percentage[stopIndex]
            iteration_count['text'] = str(
                round(tkState.cnt.cnt / 100 * p, 3)) + ' iterations'

        for button in solve_buttons:
            button['state'] = 'disabled'
        draw_animation(
            canvas, tkState.results[tkState.stop[stopIndex]], tkState.isPartial[stopIndex])
        for button in solve_buttons:
            button['state'] = 'normal'

    window = Tk()
    window.title = ("Towers of Hanoi")
    window.geometry("1000x1000")
    window.resizable(False, False)

    btn_start = Button(window, text="Start", command=tk_start)
    btn_start.place(x=100, y=800)

    btn_p1 = Button(window, text="part 1",
                    command=lambda: tk_draw_animation(0))
    btn_p1.place(x=230, y=840)
    btn_p1['state'] = 'disabled'
    btn_p2 = Button(window, text="part 2",
                    command=lambda: tk_draw_animation(1))
    btn_p2.place(x=400, y=840)
    btn_p2['state'] = 'disabled'
    btn_p3 = Button(window, text="part 3",
                    command=lambda: tk_draw_animation(2))
    btn_p3.place(x=570, y=840)
    btn_p3['state'] = 'disabled'
    btn_p4 = Button(window, text="part 4",
                    command=lambda: tk_draw_animation(3))
    btn_p4.place(x=720, y=840)
    btn_p4['state'] = 'disabled'

    btn_end = Button(window, text="Solve",
                     command=lambda: tk_draw_animation(4))
    btn_end.place(x=870, y=800)
    btn_end['state'] = 'disabled'

    solve_buttons = [btn_p1, btn_p2, btn_p3, btn_p4, btn_end]

    iteration_count = Label(window)
    iteration_count.place(x=50, y=760)

    ent1 = Entry(window)
    ent1.place(x=230, y=760)
    ent2 = Entry(window)
    ent2.place(x=400, y=760)
    ent3 = Entry(window)
    ent3.place(x=570, y=760)
    ent4 = Entry(window)
    ent4.place(x=720, y=760)
    entities = [ent1, ent2, ent3, ent4]
    canvas = Canvas(window, height=750, width=1000)
    canvas.pack()
    return window


def main():
    window = setup_tk()

    window.mainloop()


if __name__ == '__main__':
    main()
