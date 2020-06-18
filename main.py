from tkinter import *
from random import seed
from random import sample

root = Tk()
root.title('Dice_Roller')
root.iconbitmap(r"icon.ico")
root.geometry("400x200")

seed(1)

def dice_roller():
    possible_rolls = [i for i in range(die.get() + 1)] *10
    possible_rolls = [i for i in possible_rolls if i != 0]
    rolls = sample(possible_rolls, e.get())
    myLabel.config(text=rolls)
    return 0

die = IntVar()

drop = OptionMenu(root, die, 4, 6, 12, 20,)
drop.pack()

die.set(6)

e = Scale(root, from_=1, to=50, orient=HORIZONTAL)
e.pack()

myButton = Button(root, text="Roll!", command = dice_roller)
myButton.pack()

myLabel = Label(root, text="Dice rolls wil appear here")
myLabel.pack()



root.mainloop()

