from tkinter import *
from random import seed
from random import sample
from random import randint
import time

root = Tk()
root.title('Dice_Roller')
root.iconbitmap(r"icon.ico")
root.geometry("400x200")

seed(time.time())


def dice_roller():
    rolls = []
    i = 0
    while i < e.get():
        rolls.append(randint(1, die.get()))
        i += 1
    myLabel.config(text=rolls)

    pass


die = IntVar()

drop = OptionMenu(root, die, 4, 6, 12, 20, )
drop.pack()

die.set(6)

e = Scale(root, from_=1, to=50, orient=HORIZONTAL)
e.pack()

myButton = Button(root, text="Roll!", command=dice_roller)
myButton.pack()

myLabel = Label(root, text="Dice rolls wil appear here")
myLabel.pack()

root.mainloop()
