import tkinter as tk
from tkinter import Frame, Label, ttk
from tkinter.constants import LEFT, NW, RIGHT
from PIL import Image,ImageTk


news = tk.Tk()
news.title("Newspaper")
news.geometry('900x400+250+50')

def event_100(text1):
    final_text = ''
    for i in range(0,len(text1)):
        final_text += text1[i]
        if i%100==0 and i!=0:
            final_text += '\n'
    return final_text

text = []
photo = []
for i in range(0,3):
    with open(f'{i+1}.txt') as f:
        a = f.read()
        text.append(event_100(a))
    image = Image.open(f'{i+1}.jpg')
    image = image.resize((254,200))
    photo.append(ImageTk.PhotoImage(image))

f0 = Frame(news,width=800,height=0).pack()
Label(f0,text='Today Top News',font='arial 25').pack()
Label(f0,text='Sep 5, 2021',font='arial 10').pack()

f1 = Frame(news,width=900,height=0)
Label(f1,text=text[0]).pack(side=LEFT)
Label(f1,image=photo[0]).pack()
f1.pack(anchor='w',padx=10)

f2 = Frame(news,width=900,height=0)
Label(f2,text=text[1]).pack(side=RIGHT)
Label(f2,image=photo[1]).pack()
f2.pack(anchor='w',padx=10)

f3 = Frame(news,width=900,height=0)
Label(f3,text=text[2]).pack(side=LEFT)
Label(f3,image=photo[2]).pack()
f3.pack(anchor='w',padx=10)





news.mainloop()