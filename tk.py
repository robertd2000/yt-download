from tkinter import *
from tkinter import messagebox
from index import get_video

window = Tk()
window.geometry('600x350')
window.title("Скачивание видео с YouTube")


def clicked():
    res = txt.get()
    messagebox.showinfo('Alert', 'Видео скачано!')
    txt.delete(0, END)
    return get_video(res, '\\Users\\капитал\\Desktop\\udemy')


lbl1 = Label(window, text="Скачать видео", font='Times 30')
lbl1.grid(column=5, row=0)

lbl2 = Label(window, text="")
lbl2.grid(column=7, row=0)

txt = Entry(window, width=20, font='Times 30')
txt.grid(column=5, row=1)

btn = Button(window, text='Скачать', command=clicked, bg='blue', fg='white', font='Times 30')
btn.grid(column=7, row=1)

window.mainloop()

print('Hi')
