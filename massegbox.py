import tkinter as tk
from tkinter import Scale, ttk
import tkinter.messagebox as message

win =tk.Tk()
win.title('Windows')
win.geometry('800x400+200+30')


def bd():
    v1 = message.askquestion('Entry Box','Are you subscribed our chanal')
    if v1 == 'yes':
        v2 = message.askquestion('Entry Box','Are you happy to subscrib our chanal')
        if v2 == 'yes':
            message.showinfo('Thanks','Thanks')
        else:
            message.showinfo('feedback','please give me your feedback')
    else:
        message.showinfo('subscrib','subscribed our chanal')


    

ttk.Button(win,text="This is message box.",command=bd).pack()


var = Scale(win,from_=0,to=500).pack()



win.mainloop()