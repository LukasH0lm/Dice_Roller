from tkinter import *
from random import seed
from random import choice

root = Tk()
root.title('Dice_Roller')
root.iconbitmap(r"icon.ico")
root.geometry("400x400")

seed(1)

def dice_roller():
    sequence = [i for i in range(die.get())]
    rolls = choice(sequence)
    myLabel.config(text=rolls)
    return 0

die = IntVar()
die.set(6)



drop = OptionMenu(root, die, 4, 6, 12, 20)
drop.pack()

e = Entry(root, width=3)
e.pack()

myButton = Button(root, text="Roll!", command = dice_roller)
myButton.pack()

myLabel = Label(root, text="Dice rolls wil appear here")
myLabel.pack()



root.mainloop()

