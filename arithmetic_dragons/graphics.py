from tkinter import *


def vopros(quest):
    root = Tk()
    f_1 = Frame(root, width=50, height=20)
    f_2 = Frame(root, width=50, height=20)

    def start(event):
        global otvet
        otvet = ent1.get()
        close_win()

    def close_win():
        root.destroy()

    root.title('Game')
    lab = Label(f_1, text=quest, font="Arial 15")
    ent1 = Entry(f_1, width=30, bd=10)
    button = Button(f_2, text='Send', width=10, font="Arial 10")
    f_1.place(relx=0, rely=1)
    button.bind("<Button-1>", start)

    f_1.pack()
    f_2.pack()
    lab.pack()
    button.pack()
    ent1.pack()
    root.mainloop()
    return otvet


def message(mess, color="yellow"):
    root = Tk()

    def start(event):
        close_win()

    def close_win():
        root.destroy()

    root.title('')
    lab = Label(root, text=mess, font="Arial 20")
    button = Button(root, text='OK', width=19, bg=color, fg="white", font="Arial 10")
    button.bind("<Button-1>", start)

    lab.pack()
    button.pack()
    root.mainloop()
