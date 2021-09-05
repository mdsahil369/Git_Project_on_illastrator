import tkinter as tk
from tkinter import StringVar, ttk
from tkinter import colorchooser
from tkinter.constants import LEFT, N, NW

root = tk.Tk()
root.title("illastrator")
canvas_w = 800
canvas_h = 400
root.geometry(f'{canvas_w}x{canvas_h}+200+50')

canvas_wd = tk.Canvas(root, width=canvas_w, height=350, background="grey")
canvas_wd.pack()


color = ['']


def line():
    li = []

    def sahil(event):
        li.append(event.x)
        li.append(event.y)

    def sahil2(event):
        li.append(event.x)
        li.append(event.y)
        if color[-1] == '':
            c = 'black'
        else:
            c = color[-1]
        canvas_wd.create_line(li[0], li[1], li[2], li[3], fill=c)
        li.pop()
        li.pop()
        li.pop()
        li.pop()

    root.bind('<Button>', sahil)
    root.bind('<ButtonRelease>', sahil2)


def rectangle():
    li = []

    def sahil(event):
        li.append(event.x)
        li.append(event.y)

    def sahil2(event):
        li.append(event.x)
        li.append(event.y)
        canvas_wd.create_rectangle(
            li[0], li[1], li[2], li[3], fill=f'{color[-1]}')
        li.pop()
        li.pop()
        li.pop()
        li.pop()

    root.bind('<Button>', sahil)
    root.bind('<ButtonRelease>', sahil2)


def oval():
    li = []

    def sahil(event):
        li.append(event.x)
        li.append(event.y)

    def sahil2(event):
        li.append(event.x)
        li.append(event.y)
        canvas_wd.create_oval(li[0], li[1], li[2], li[3], fill=f'{color[-1]}')
        li.pop()
        li.pop()
        li.pop()
        li.pop()

    root.bind('<Button>', sahil)
    root.bind('<ButtonRelease>', sahil2)
# def write():
#     li = []
#     def move(event):
#         li.append(event.x)
#         li.append(event.y)
#         if len(li) == 4:
#             canvas_wd.create_line(li[0],li[1],li[2],li[3])
#             li.pop()
#             li.pop()
#             li.pop()
#             li.pop()

#     root.bind('<Motion>', move)


def clear():
    canvas_wd.delete('all')


def color_c():
    colorw = tk.colorchooser.askcolor()
    color.append(colorw[1])


line_button = ttk.Button(root, text="line", command=line)
rect_button = ttk.Button(root, text="rect", command=rectangle)
oval_button = ttk.Button(root, text="oval", command=oval)
# write_button = ttk.Button(root,text="write",command=write)
color_button = ttk.Button(root, text="color", command=color_c)
clear_button = ttk.Button(root, text="clear", command=clear)

line_button.pack(side=LEFT)
rect_button.pack(side=LEFT)
oval_button.pack(side=LEFT)
# write_button.pack(side=LEFT)
color_button.pack(side=LEFT)
clear_button.pack(side=LEFT)


root.mainloop()
