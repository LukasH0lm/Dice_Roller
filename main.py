from tkinter import *
from random import seed
from random import sample

root = Tk()
root.title('Dice_Roller')
root.iconbitmap(r"icon.ico")
root.geometry("400x400")

seed(1)

#def setdie(selected_die):
#    user_die= 

def dice_roller():
    sequence = [i for i in range(die.get())] *10
    rolls = sample(sequence, e.get())
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

