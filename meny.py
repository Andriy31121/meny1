from customtkinter import *
from random import *

def show_win():
    win2 = CTk()
    win2.geometry('100x100')
    win2.title('соціальне опитуваня')
    label_win = CTkLabel('дуже приємно чути!!!!!')
    win2.mainloop()










win = CTk()
win.geometry('500x500')
win.title('соціальне опитуваня')

lbl = CTkLabel(win, text="чи подобається тобі в логіці????")
lbl.pack(pady=20)

def btn_no_func():
    new_x = random(0, win.winfo_width() - btn_no.winfo_width())
    new_y = random(0, win.winfo_height() - btn_no.winfo_height())
    btn_no.place(x=new_x)
    btn_no.place(y=new_y)
def btn_func():
    new_x = random(0, win.winfo_width() - btn_no.winfo_width())
    new_y = random(0, win.winfo_height() - btn_no.winfo_height())
    btn_no.place(x=new_x)
    btn_no.place(y=new_y)



btn_yes = CTkButton(win, text="так", compound=show_win)
btn_yes.place(x=60, y=100)

btn_no = CTkButton(win, text="ні", command=btn_no_func)
btn_no.place(x=200, y=100)


win.mainloop()
