#import the required libraries
#tkinter library to create kickass GUI
#random library because we're randomly selecting numbers maybe
from tkinter import Tk, Label, Button
import random
 
#create tkinter instance, because behind the scenes it all object oriented
root=Tk()
#define the length and height of the gui window to be displayed
root.geometry("550x400")
 
#GUI will have two basic components
#1.Button which will trigger the rolling of dice
#2.Dice label and a dice variable which the variable can be used to expand
# the program.
#3 
l1 = Label(root, font=("Helvetica",30))
l2 = Label(root, font=("Helvetica",30))
l3 = Label(root, font=("Helvetica",30))
l4 = Label(root, font=("Helvetica",30))

l2 = Label(root, font=("Helvetica",30))
l3 = Label(root, font=("Helvetica",30))
l4 = Label(root, font=("Helvetica",30))
l5 = Label(root, font=("Helvetica",30))
l6 = Label(root, font=("Helvetica",30))
l7 = Label(root, font=("Helvetica",30))
l8 = Label(root, font=("Helvetica",30))
spacer = Label(root, text="          ", font=("Helvetica",30))
def roll():
    #create a number variable in which the list of all the ASCII characters of the string will be stored
    #Use backslash because unicode must have a backslash 
    dicedict = { '1' : '\u2680','2' :'\u2681', '3' : '\u2682', '4' :'\u2683', '5' :'\u2684', '6' : '\u2685'}
    #configure the label and assoicate it with a dictionary
    #called dicedict and randomly picking from it
    
    var1 = random.choice(list(dicedict.items()))
    var2 = random.choice(list(dicedict.items()))
    var3 = random.choice(list(dicedict.items()))
    var4 = random.choice(list(dicedict.items()))
    var5 = random.choice(list(dicedict.items()))
    var6 = random.choice(list(dicedict.items()))
    var7 = random.choice(list(dicedict.items()))
    var8 = random.choice(list(dicedict.items()))

###below shows the result of the dice roll

    l1.config(text = var1)
    l2.config(text = var2)
    l3.config(text = var3)
    l4.config(text = var4)
    l5.config(text = var5)
    l6.config(text = var6)
    l7.config(text = var7)
    l8.config(text = var8)
# below is the position on the screen using rows and columns
    
    l1.grid(row=4, column=1)
    l2.grid(row=5, column=1)
    l3.grid(row=6, column=1)
    l4.grid(row=7, column=1)
    l5.grid(row=4, column=3)
    l6.grid(row=5, column=3)
    l7.grid(row=6, column=3)
    l8.grid(row=7, column=3)
    spacer.grid(row=0, column=2)
    # below separates the key from value so it can be use in a conditional
    # for a future program that needs dice roll to get somthing to happen
    key1, val1 = var1
    key2, val2 = var2
    key3, val3 = var3
    key4, val4 = var4
    key5, val5 = var5
    key6, val6 = var6
    key7, val7 = var7
    key8, val8 = var8
    # print function to test if that worked
    print(key1)
    
b1 = Button(root, text="Roll them bones!",background="orange", foreground='blue', border=7, command=roll)
b1.grid(row=0, column=0)
 
root.mainloop()
